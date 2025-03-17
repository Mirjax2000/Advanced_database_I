from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    """Book model"""

    title = models.CharField(
        max_length=32,
        verbose_name="Nazev knihy",
        null=False,
        blank=False,
        unique=True,
    )
    description = models.TextField(
        null=False, blank=True, verbose_name="Popis knihy"
    )
    pages = models.IntegerField(
        verbose_name="Pocet stranek",
        null=False,
        blank=False,
        validators=[MinValueValidator(10), MaxValueValidator(1000)],
    )
    is_bestseller = models.BooleanField(
        default=False, verbose_name="Je to bestseller?:"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="vytvoreno",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="update zaznamu",
    )
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        """Meta funkce na ordering"""

        ordering = ["title"]

    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self) -> str:
        return f"Book(ID={self.pk},title='{self.title}', pages={self.pages}, Bestseller={self.is_bestseller})"

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
