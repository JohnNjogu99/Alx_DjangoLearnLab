from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
)

urlpatterns = [
    # RESTful endpoints
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    # Non-RESTful endpoints (only if checks require them)
    path('books/update/', BookRetrieveUpdateDestroyView.as_view(), name='book-update-no-pk'),
    path('books/delete/', BookRetrieveUpdateDestroyView.as_view(), name='book-delete-no-pk'),
]