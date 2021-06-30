import re
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from rest_framework import renderers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from .serializers import Contact_form_se
from django.views.decorators.csrf import csrf_exempt 
from .forms import ContactForm

def index(request):
    return render(request,'woodogdata/index.html')


#This View is handeled for submitting contact form data with a REST _ API 
@csrf_exempt
def contact_us(request): 
 if request.method=='POST':
  try:
    complex_data=request.body
    print(complex_data)
    print(type(complex_data))
    print("got the first print !")
    stream_data=io.BytesIO(complex_data)
    print(stream_data)
    python_data=JSONParser().parse(stream_data)
    print(python_data)
    serialization_ofdata=Contact_form_se(data=python_data)
    print(serialization_ofdata)
    print("bes eto ta tokkoi !")
    if serialization_ofdata.is_valid():
        serialization_ofdata.save()
        print("process done succesfully.........!")
        msg={'done_msg':'Data has been sucessfully created and submitted!'}
        json_msg=JSONRenderer().render(msg)
        return render(request,'woodogdata/contact_us.html',{'msg':json_msg})
    else:
        error_msg=JSONRenderer().render(serialization_ofdata.errors)
        print(error_msg)
        print('data is not validated !')
        msg={'done_msg':'Error Occure During handeling data '}
        json_msg=JSONRenderer().render(msg)
        return HttpResponse('not validated !')
  except:
    return HttpResponse("Not submitted properly !")

 else:  
    forms=ContactForm()
    return render(request,'woodogdata/contact_us.html',{'form':forms})

@csrf_exempt
def contat_us_throughwebsite(request):
  if request.method =='GET':
    return render(request,'woodogdata/contact_us.html')
    return HttpResponse("done!")

  else:
   try:
    json_body=request.body
    print(json_body)
    print('the input data !')
    body=io.BytesIO(json_body)
    print(body)
    python_data=JSONParser().parse(body)
    print(python_data)
    print('Done!')
    serialization_ofdata=Contact_form_se(data=python_data)
    print(serialization_ofdata)
    print("Form fo intra sharing is working !")
    if serialization_ofdata.is_valid():
        serialization_ofdata.save()
        print("process done succesfully.........!")
        resp={'response':contatct_form_submitted}
        #return JsonResponse(resp)
        return render(request,'woodogdata/contact_us.html' ,{'msg22':'submitted succesfully !'})

       
    else:
        error_msg=JSONRenderer().render(serialization_ofdata.errors)
        print(error_msg)
        print('data is not validated !')
        msg={'done_msg':'Error Occure During handeling data '}
        json_msg=JSONRenderer().render(msg)
        return HttpResponse('not validated !')
   except:
        return HttpResponse("Not submitted properly !")
  
