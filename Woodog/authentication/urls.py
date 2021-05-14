from django.utils import regex_helper
from .views import EmailValidationView, RegistrationView, UsernameValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register',RegistrationView.as_view(), name='register'),
    path("validate-username", csrf_exempt(UsernameValidationView.as_view()), 
    name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), 
    name="validate-email"),
]
