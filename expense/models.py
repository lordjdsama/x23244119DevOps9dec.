"""
This module contains models for the 'expense' app.
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Expense(models.Model):
    """
    Model representing an expense entry.
    """
    date = models.DateTimeField(auto_now_add=True)
    expense = models.CharField(max_length=9)
    on = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """
        Returns the URL to access a detail record for this expense.
        """
        return reverse("expense-detail", kwargs={"pk": self.pk})

    def __str__(self):
        """
        String for representing the Expense object.
        """
        return f"{self.date}"
