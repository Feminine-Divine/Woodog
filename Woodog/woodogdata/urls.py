from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='woodogdata'),
    path('login/', views.login, name='woodogdata'),
]
