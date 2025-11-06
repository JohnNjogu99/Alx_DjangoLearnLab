from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based View to list all books
def list_books(request):
    # Query all book objects from the database
    books = Book.objects.all()

    # Render the 'list_books.html' template and pass the books in context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based View to show library details
class LibraryDetailView(DetailView):
    model = Library                      # Tell Django this view works with the Library model
    template_name = 'relationship_app/library_detail.html'   # Template to display
    context_object_name = 'library'      # Name of the object in the template
