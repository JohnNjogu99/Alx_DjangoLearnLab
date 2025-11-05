from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from relationship_app.models import Book, Library

# ✅ Use ListView instead of function-based view
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'  # The variable used in the template

# ✅ DetailView remains correct
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
