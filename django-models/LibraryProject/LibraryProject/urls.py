"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include  # include is required!
from django.contrib.auth import views as auth_views  # ✅ This line is missing
from relationship_app.views import add_book, edit_book, delete_book



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include URLs from relationship_app
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('books/add/', add_book, name='add_book'),  # ✅ Add book
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),  # ✅ Edit book
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),  # ✅ Delete book
]
