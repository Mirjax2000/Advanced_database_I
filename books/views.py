from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from books.models import Book


def index(request) -> HttpResponse:
    """Home page"""
    context: dict = {"result": Book.objects.all()}

    return render(request, "index.html", context)


# chybova templeta
def custom_404(request, exception):
    """404"""
    html = render_to_string("404.html", {"message": str(exception)})
    return HttpResponseNotFound(html)


# Create your views here.
