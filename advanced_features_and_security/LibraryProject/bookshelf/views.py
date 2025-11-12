from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# bookshelf/views.py

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # logic to create a book
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # logic to edit book
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # logic to delete book
    return render(request, 'delete_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
