from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='woodogdata'),

    path('contact/',views.contact_us,name='contact_us'),
    path('contact_usw/',views.contat_us_throughwebsite,name='contact_us_throughwebsite'),

    path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),

]
