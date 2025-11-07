from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path, include
from relationship_app.views import admin_view, librarian_view, member_view
from relationship_app.views import add_book, edit_book, delete_book

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view'),  # ✅ Admin route
    path('librarian-view/', librarian_view, name='librarian_view'),  # ✅ Librarian route
    path('member-view/', member_view, name='member_view'),  # ✅ Member route
    path('books/add/', add_book, name='add_book'),  # ✅ Add book
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),  # ✅ Edit book
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),  # ✅ Delete book
]
