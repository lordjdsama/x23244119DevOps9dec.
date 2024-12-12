"""
URL configuration for the expense application.

This module defines the URL patterns for the expense app, mapping views to their respective URLs.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name="expense-home"),
    path('expense/<int:pk>', views.ExpenseDetailView.as_view(), name="expense-detail"),
    path('expense/create', views.ExpenseCreateView.as_view(), name="expense-create"),
    path('expense/<int:pk>/update', views.ExpenseUpdateView.as_view(), name="expense-update"),
    path('expense/<int:pk>/delete', views.ExpenseDeleteView.as_view(), name="expense-delete"),
    path('about/', views.about, name="expense-about"),
]
