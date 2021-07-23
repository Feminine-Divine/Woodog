from django.db import models
from django.utils.text import slugify
import string
import random

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res


def Generate_slug(text):
    new_slug=slugify(text)
    from woodogdata.models import BlogModel
    print(BlogModel.objects.filter(slug=new_slug).first())
    if BlogModel.objects.filter(slug=new_slug).first():
        Generate_slug(text+generate_random_string(5))
    return new_slug