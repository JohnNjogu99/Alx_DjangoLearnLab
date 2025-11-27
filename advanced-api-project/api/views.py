from rest_framework import generics, filters, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly


class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all books (GET) and creating a new book (POST).
    Includes advanced query capabilities:
    - Filtering by title, author, and publication_year
    - Searching by title and author name
    - Ordering by title and publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # 👈 only authenticated users can list/create


    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['publication_year']  # default ordering


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single book.
    - GET /api/books/<id>/ → retrieve book
    - PATCH/PUT /api/books/<id>/ → update book
    - DELETE /api/books/<id>/ → delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only authenticated users can modify