from django.urls import path
from . import views
from .views import *
from .views import AddBlogView


urlpatterns = [
    path('', views.index, name='woodogdata'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),
    path('service/', views.service, name='service'),
    path('blog_content/<slug>', views.blog_content, name='blog_content'),
    path('feedback/',views.feedback,name='feedback'),
    path('add-blog/' ,AddBlogView.as_view(), name='add_blog'),
]
