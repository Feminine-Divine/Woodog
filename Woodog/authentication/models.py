from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_status(models.Model) : 
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	is_helper = models.BooleanField(default=False) 
	is_seeker = models.BooleanField(default=False) 

	def save(self) : 
		if self.is_seeker == False or self.is_helper == False : 
			super().save()

	def __str__(self) : 
		return self.user.username
