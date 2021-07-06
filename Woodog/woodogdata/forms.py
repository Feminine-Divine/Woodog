from django import forms
from django.forms import ModelForm
from .models import ContactModel

class ContactForm(forms.ModelForm):
   class Meta:
    model=ContactModel
    fields='__all__'
