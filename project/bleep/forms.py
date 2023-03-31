from django import forms
from django.forms import ModelForm
from .models import InteresanteLink 
from tinymce.widgets import TinyMCE

class LinkForm(ModelForm):

    class Meta:
        model =  InteresanteLink
        fields = ["titel","beschrijving","link",]