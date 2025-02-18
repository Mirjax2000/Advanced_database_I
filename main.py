import os

import django

# Nastavení Django prostředí
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybooks.settings")
django.setup()

from books.models import Book

Book.objects.create(title="Kamna jak hovado", pages=150)

ferda = Book.objects.get(title="Ferda")

print(ferda.title, ferda.is_bestseller)
