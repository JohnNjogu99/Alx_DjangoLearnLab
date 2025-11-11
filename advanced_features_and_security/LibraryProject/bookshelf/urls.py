from django.urls import path
from .views import LibraryDetailView

urlpatterns = [
    path('book/<int:pk>/', LibraryDetailView.as_view(), name='book_detail'),
]
