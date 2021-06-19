from os import link
import re
from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from authentication.models import User_status
import json

from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text , DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from django.contrib import auth


# Create your views here.

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid.'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry, Email already in use.'}, status=409)
        return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters.'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry, Username already in use.'}, status=409)
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request , type_of = None):
        params = { 'txt' : type_of }
        return render(request,'authentication/register.html'  , params)

    def post(self, request , type_of = None):
        #create a user account

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        choice = type_of
        params  = {'txt' : type_of}

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<6:
                    messages.error(request,'Password is too short')
                    return render(request, 'authentication/register.html')
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                if choice == 'helper' : 
                    user_status = User_status(user = user , is_helper  = True)
                elif choice == 'seeker' : 
                    user_status = User_status(user = user , is_seeker = True)
                user_status.save()

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('activate',kwargs={'uidb64':uidb64,'token': token_generator.make_token(user)})

                email_subject = 'Activate your account'
                activate_url = 'http://'+domain+link
                email_body = 'Hi, '+ user.username + \
                    ' Please use this link to verify your account\n'+ activate_url
                email = EmailMessage(
                email_subject,
                email_body,
                'from@example.com',
                [email],
                )
                email.send(fail_silently=False)
                messages.success(request,'Account successfully created')
                return render(request, 'authentication/register.html' , params)
                
        return render(request,'authentication/register.html' , params)

class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user,token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')
        except Exception as ex:
            pass

        
        return redirect('login')

class LoginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:

            user = auth.authenticate(username=username , password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' + 
                                    user.username + ' you are now logged in')
                    return redirect('woodogdata')

                messages.error(
                    request, 'Account is not active, please check your email')
                return render(request,'authentication/login.html')
            messages.error(
                request, 'Invalid credentials, try again')
            return render(request,'authentication/login.html')
        messages.error(
            request, 'Please fill all the fields')
        return render(request,'authentication/login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')
            
                
def get(self, request):
        return render(request,'authentication/register.html')