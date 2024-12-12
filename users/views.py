"""
Views for handling user registration and profile display in the users app.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required  # pylint: disable=wrong-import-order


def register(request):
    """
    Handle user registration.

    If the request method is POST, process the registration form and save the user
    if the form is valid. Display a success message and redirect to the login page.
    Otherwise, render the registration form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered registration page or a redirect to the login page.
    """
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")  # pylint: disable=unused-variable
            messages.success(request, f"{username}, account created")
            return redirect("users-login")
    else:
        form = forms.UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required()
def profile(request):
    """
    Display the profile page for the logged-in user.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page.
    """
    return render(request, "users/profile.html")
