from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from .validators import file_size

class Video(models.Model):
    titel=models.CharField(max_length=200)
    beschrijving = models.TextField(blank=True,)
    video=models.FileField(upload_to="video/%y/%m", validators=[file_size])
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self): 
        return self.titel

class Analyse(models.Model):
    titel=models.CharField(max_length=200)
    evaluatie=models.TextField()
    suggestie=models.TextField(blank=True)
    video = models.ForeignKey(Video,default="", verbose_name="video", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self): 
        return self.titel