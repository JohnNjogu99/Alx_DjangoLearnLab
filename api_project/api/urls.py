# api/urls.py
from django.urls import path  # <-- 'path' must be explicitly imported
from .views import BookList   # <-- 'BookList.as_view' must be used below

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # <-- This line must include 'BookList.as_view'
]
