from django import forms
from django.forms import ModelForm
from .models import ArticleSeries, Article, Contact
from tinymce.widgets import TinyMCE
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class SeriesCreateForm(forms.ModelForm):
    
    class Meta:
        model = ArticleSeries
        fields = ["publish","title","subtitle","slug","image",]
 
class ArticleCreateForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ["publish","title","subtitle","article_slug","content","notes","series","image",]

class SeriesUpdateForm(forms.ModelForm):
    
    class Meta:
        model = ArticleSeries
        fields = ["publish","title","subtitle","image",]
 
class ArticleUpdateForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ["publish","title","subtitle","content","notes","series","image",] 


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")    

 

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname','lastname','email','information','reden']

    captcha = ReCaptchaField(widget = ReCaptchaV2Checkbox())