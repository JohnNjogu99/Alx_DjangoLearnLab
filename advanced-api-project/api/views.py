from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework


# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """
    Provides a read-only list of all books.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # applies custom permission


# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Provides details of a single book by ID.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    Includes validation from BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookListView(generics.ListAPIView):
    """
    Provides a list of all books with advanced query capabilities:
    - Filtering by title, author, and publication_year
    - Searching by title and author name
    - Ordering by title and publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']
        # Search fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['publication_year']  # default ordering
