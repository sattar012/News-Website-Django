from django import forms
from django.forms.fields import DateField

from news.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {



        }
