"""
Created: Daniel Swain
Date: 13/11/2016

Where models and objects are registered to the Admin console for editing at localhost:8000/admin."""

from django.contrib import admin

from .models import Question, Choice

# Register the Question and Choice models to the Admin page.
admin.site.register(Question)
admin.site.register(Choice)