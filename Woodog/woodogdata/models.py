from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name=models.CharField(max_length=60,default='name')
    email=models.CharField(max_length=60,default='mail')
    contact_no=models.CharField(max_length=12,default='number bro ')
    message=models.TextField(max_length=500,default='message!')

    def __str__(self):
        return str(self.name)
         
