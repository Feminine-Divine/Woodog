from django.db import models
from django.contrib.auth.models import User
from authentication.models import User_status
from django.utils import timezone

# Create your models here.

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

#Models for adding pictures to gallery page
class Gallery(models.Model):
    tag=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    title=models.CharField(max_length=100)
    uploading_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploading_date']