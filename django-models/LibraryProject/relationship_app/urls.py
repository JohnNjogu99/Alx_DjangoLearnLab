from django.urls import path
from relationship_app.views import BookListView, LibraryDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
