from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json

# Create your views here.

class UsernameValidationView(View):
    def get(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'})
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request):
        return render(request,'authentication/register.html')