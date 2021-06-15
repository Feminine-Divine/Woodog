from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='woodogdata'),
    path('sign-up/',views.signup, name='woodogdata')
]
