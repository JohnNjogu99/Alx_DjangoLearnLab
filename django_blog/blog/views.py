from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm

# Registration view
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()          # Save new user
            login(request, user)        # Log them in immediately
            return redirect("profile")  # Redirect to profile page
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

# Profile view (requires login)
@login_required
def profile(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")
    return render(request, "profile.html", {"user": request.user})

# Login view using Django's built-in class
class CustomLoginView(LoginView):
    template_name = "login.html"

# Logout view using Django's built-in class
class CustomLogoutView(LogoutView):
    template_name = "logout.html"
