from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("books", views.BooksView.as_view(), name="book_list"),
    path("books/<slug:slug>", views.OneBook.as_view(), name="one_book"),
    path("books/create/", views.BookCreateView.as_view(), name="book_create"),
    path("form", views.ContactFormView.as_view(), name="form_view"),
]
