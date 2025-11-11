from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book

class LibraryDetailView(DetailView):
    model = Book
    template_name = 'bookshelf/book_detail.html'  # your template
    context_object_name = 'book'

# Create your views here.
