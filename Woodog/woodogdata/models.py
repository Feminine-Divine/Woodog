from django.db import models
from django.contrib.auth.models import User
from authentication.models import User_status
from django.utils import timezone

# Create your models here

# Seekers posting condition
class Seeker_Post(models.Model):
    user_status = models.ForeignKey(User_status,  on_delete = models.CASCADE)
    condition = models.TextField()
    location = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['-timestamp']

# For Helpers and Seekers to interact
class Comment(models.Model):
    post_connect = models.ForeignKey(Seeker_Post, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete =  models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author.username

    class Meta:
        ordering = ['-timestamp']
        
# For Contact Us Form
class ContactModel(models.Model):
    name=models.CharField(max_length=60,default='name')
    email=models.CharField(max_length=60,default='mail')
    contact_no=models.CharField(max_length=12,default='number bro ')
    message=models.TextField(max_length=500,default='message!')

    def __str__(self):
        return str(self.name)

