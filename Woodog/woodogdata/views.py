from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

# @login_required(login_url='/authentication/login')
def index(request):
    crr_user = request.user 
    if User.objects.filter(username = crr_user).exists() : 
        crr_user = User.objects.get(username = crr_user)
        if not crr_user.is_staff and not crr_user.is_superuser and crr_user.is_active :  
            params = {'success' : True , 'name' : crr_user}
            return render(request, 'woodogdata/index.html' , params)
        return render(request, 'woodogdata/index.html')
    else: 
        return render(request,'woodogdata/index.html')
