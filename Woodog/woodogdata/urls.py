from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='woodogdata'),
<<<<<<< HEAD
    path('contact/',views.contact_us,name='contact_us'),
    path('contact_usw/',views.contat_us_throughwebsite,name='contact_us_throughwebsite'),
=======
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
>>>>>>> d98ff40ce3abff4410dd434228ea4ce5bc49b0b2
]
