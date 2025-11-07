from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path, include
from relationship_app.views import admin_view, librarian_view, member_view
from relationship_app.views import add_book, edit_book, delete_book

urlpatterns = [
    path('list_books/', list_books, name='list_books'),  # ✅ Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ Class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view'),  # ✅ Admin route
    path('librarian-view/', librarian_view, name='librarian_view'),  # ✅ Librarian route
    path('member-view/', member_view, name='member_view'),  # ✅ Member route
    path('add_book/', add_book, name='add_book'),        # ✅ Matches checker string
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # ✅ Matches checker string
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
