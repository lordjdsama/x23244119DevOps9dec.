"""
Admin module for managing Expense models in the Django admin interface.
"""

# pylint: disable=import-error
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Expense)
