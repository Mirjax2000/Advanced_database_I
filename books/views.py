"""Views"""

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
)

from .forms import ContactForm
from .models import Book


# Create your views here.
class BookCreateView(CreateView):
    """Formular"""

    model = Book
    template_name = "form.html"
    fields = ["title", "pages", "is_bestseller"]

    def get_success_url(self):
        title = self.object.title
        slug = slugify(title)
        return reverse_lazy("one_book", args=[slug])


class IndexView(TemplateView):
    """Index view"""

    template_name = "index.html"
    extra_context = {"hero": "Vigokiller"}


class BooksView(ListView):
    """Movies view"""

    model = Book
    template_name = "list.html"
    context_object_name = "books"


class OneBook(DetailView):
    """One movie detail"""

    model = Book
    template_name = "one_book.html"
    context_object_name = "book"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class ContactFormView(FormView):
    """Form view"""

    template_name = "form.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")
