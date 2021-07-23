from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import BlogModel,Gallery

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
    gallery = Gallery.objects.all()
    gallery_dict = {}
    gallery_title = {}

    for img in gallery:
        if img.tag not in gallery_dict.keys():
            gallery_dict[img.tag] = []
        gallery_dict[img.tag].append(img)
    print(gallery_dict)
    context = {'gallery_dict': gallery_dict}
    return render(request,'woodogdata/gallery.html',context)

def blog(request):
    context = {'trending_first':BlogModel.objects.all().filter(tag='trending_first'),
    'trending' : BlogModel.objects.all().filter(tag='trending'),
    'latest':BlogModel.objects.all().filter(tag='latest'),
    'editor1':BlogModel.objects.all().filter(tag='editor1'),
    'editor2':BlogModel.objects.all().filter(tag='editor2'),
    'popular':BlogModel.objects.all().filter(tag='popular')}
    return render(request , 'woodogdata/blog.html' , context)

def faq(request):
    return render(request,'woodogdata/faq.html')    

def service(request):
    return render(request,'woodogdata/service.html') 

def blog_content(request,slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request,'woodogdata/blog_content.html',context)

def feedback(request):
    return render(request,'woodogdata/feedback.html') 