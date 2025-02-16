from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


# chybova templeta
def custom_404(request, exception):
    html = render_to_string("404.html", {"message": str(exception)})
    return HttpResponseNotFound(html)


# Create your views here.
