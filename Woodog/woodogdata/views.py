from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# @login_required(login_url='/authentication/login')

def index(request):
    crr_user = request.user
    try : 
        crr_user = User.objects.get(username = crr_user)
        if crr_user.is_active : 
            params = {'success' : True , 'name' : crr_user}
        else : 
            params = {'success' : False , 'name' : crr_user}
        return render(request, 'woodogdata/index.html' , params )
    except : 
        return render(request, 'woodogdata/index.html' )


def about(request):
    return render(request,'woodogdata/about.html')

def contact(request):
    return render(request,'woodogdata/contact.html')

def gallery(request):
    return render(request,'woodogdata/gallery.html')

def blog(request):
    return render(request,'woodogdata/blog.html')

def faq(request):
    return render(request,'woodogdata/faq.html')    

def service(request):
    return render(request,'woodogdata/service.html') 

def blog_content(request):
    return render(request,'woodogdata/blog-content.html') 
