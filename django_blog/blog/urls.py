from django.urls import path
from django.urls import include
from .views import register, profile, CustomLoginView, CustomLogoutView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]
