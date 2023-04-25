from django.urls import path

from . import views

urlpatterns = [
    path("", views.ping, name="ping"),
    path("books/", views.BooksRelatedView.as_view(), name="books"),
]

