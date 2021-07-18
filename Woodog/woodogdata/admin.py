from django.contrib import admin
from .models import Seeker_Post, Comment, BlogModel
from .models import Seeker_Post, Comment,Gallery


# Register your models here.
admin.site.register(Seeker_Post)
admin.site.register(Comment)
admin.site.register(BlogModel)
admin.site.register(Gallery)

