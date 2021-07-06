from rest_framework import serializers
from .models import ContactModel
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

class Contact_form_se(serializers.Serializer):
    name=serializers.CharField(max_length=60)
    email=serializers.CharField(max_length=60)
    contact_no=serializers.CharField(max_length=20)
    message=serializers.CharField(max_length=500) 

    def create(self,validate_data):
     return ContactModel.objects.create(**validate_data)