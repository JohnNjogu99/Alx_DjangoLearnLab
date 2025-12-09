# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, ProfileForm


def register_view(request):
    """
    Show registration form and create user on valid POST.
    After registration we optionally log the user in and redirect to profile.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    """
    View and update the authenticated user's basic profile (first/last/email).
    Handles GET and POST.
    """
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})
