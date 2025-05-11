"""
URL mapping for the ATLAS app.
This module defines the URL patterns for the ATLAS app, 
including the landing page and any other views that may be added in the future.
The URL patterns are defined using Django's path function,
which maps URLs to views.
The landing page is mapped to the 'landing' view in the views module of the ATLAS app.
The URL patterns are included in the main URL configuration of the Django project.
"""

from django.urls import path
from ATLAS import views

app_name = 'ATLAS'
urlpatterns = [
    path('', views.landing, name='landing'),
]