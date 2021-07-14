from django.utils import regex_helper
from .views import EmailValidationView, Reset_Newpassword_form, Forget_PasswordView, Password_reset_form, LoginView, ChangePasswordView, LogoutView, RegistrationView, UsernameValidationView, VerificationView
from django.urls import path
from authentication import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('register/<str:type_of>',RegistrationView.as_view(), name='register'),
    path('login',LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('forget_password',Forget_PasswordView.as_view(), name='forget_password'),
    path("reset-password/<uidb64>/<token>", Password_reset_form.as_view() , name='reset-password'),
    path("validate-username", csrf_exempt(UsernameValidationView.as_view()), 
    name="validate-username"),
    path('reset-password', Reset_Newpassword_form.as_view(), name='reset-password'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), 
    name="validate-email"),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate'),
    path('set-newpassword/',login_required(views.ChangePasswordView.as_view(),login_url='login'), name='set-newpassword'),
 ]
