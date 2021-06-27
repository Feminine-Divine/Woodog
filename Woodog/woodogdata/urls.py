from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='woodogdata'),
    path('contact/',views.contact_us,name='contact_us'),
]
