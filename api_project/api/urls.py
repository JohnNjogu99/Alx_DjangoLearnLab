# api/views.py
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()          # what data to return
    serializer_class = BookSerializer      # how to convert data to JSON
