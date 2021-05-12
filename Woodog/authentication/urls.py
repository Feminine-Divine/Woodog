from django.utils import regex_helper
from .views import RegistrationView
from django.urls import path

urlpatterns = [
    path('register',RegistrationView.as_view(), name='register')
]
