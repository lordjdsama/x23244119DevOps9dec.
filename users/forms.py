"""
Forms for the users app, including user registration.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):  # pylint: disable=too-few-public-methods
    """
    Form for registering a new user, extending Django's UserCreationForm.
    Adds an email field to the default fields.
    """
    email = forms.EmailField()

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Metadata for UserRegisterForm, specifying the User model and form fields.
        """
        model = User
        fields = ["username", "email", "password1", "password2"]
