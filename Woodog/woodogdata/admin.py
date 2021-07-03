from django.contrib import admin
from .models import Seeker_Post, Comment, ContactModel

# Register your models here.
admin.site.register(Seeker_Post)
admin.site.register(Comment)
admin.site.register(ContactModel)
