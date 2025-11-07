from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.urls import path, include
from relationship_app.views import admin_view, librarian_view, member_view

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view'),  # ✅ Admin route
    path('librarian-view/', librarian_view, name='librarian_view'),  # ✅ Librarian route
    path('member-view/', member_view, name='member_view'),  # ✅ Member route
]
