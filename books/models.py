from django.db import models


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
    pages = models.IntegerField(
        verbose_name="Pocet stranek", null=False, blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="vytvoreno",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="update zaznamu",
    )

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"Book(title='{self.title}', pages={self.pages})"
