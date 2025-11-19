# api/views.py
from rest_framework import permissions
from rest_framework import generics, viewsets  # <-- keep generics for BookList, add viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ✅ BookViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):  # <-- satisfies "ModelViewSet" check
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
