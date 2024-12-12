"""
Views for managing expenses in the expense tracker app.
"""

from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models


def home(request):
    """
    Display the home page with a list of all expenses.
    """
    expense = models.Expense.objects.all()  # pylint: disable=no-member
    context = {"expense": expense}
    return render(request, "expense/home.html", context)


class ExpenseListView(ListView):
    """
    View to list all expenses.
    """
    model = models.Expense
    template_name = "expense/home.html"
    context_object_name = "expense"


class ExpenseDetailView(LoginRequiredMixin, DetailView):  # pylint: disable=too-many-ancestors
    """
    View to display details of a single expense.
    """
    model = models.Expense


class ExpenseCreateView(LoginRequiredMixin, CreateView):  # pylint: disable=too-many-ancestors
    """
    View to create a new expense.
    """
    model = models.Expense
    fields = ["expense", "on"]

    def form_valid(self, form):
        """
        Automatically set the author of the expense to the current user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # pylint: disable=too-many-ancestors
    """
    View to update an existing expense.
    """
    model = models.Expense
    fields = ["expense", "on"]

    def test_func(self):
        """
        Ensure that only the author of the expense can update it.
        """
        expense = self.get_object()
        return self.request.user == expense.author

    def form_valid(self, form):
        """
        Automatically set the author of the expense to the current user during update.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class ExpenseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # pylint: disable=too-many-ancestors
    """
    View to delete an expense.
    """
    model = models.Expense
    success_url = reverse_lazy("expense-home")

    def test_func(self):
        """
        Ensure that only the author of the expense can delete it.
        """
        expense = self.get_object()
        return self.request.user == expense.author


def about(request):
    """
    Display the 'About' page.
    """
    return render(request, "expense/about.html")
