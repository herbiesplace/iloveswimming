from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

from django.template.defaultfilters import slugify
import os

REDEN= [
        ('vraag', 'vraag'),
        ('opmerking','opmerking'),
        ('suggestie','suggestie'),
        ('probleem','probleem')
    ]

class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)
    publish = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/noimage.jpg',upload_to=image_upload_to, max_length=255)


    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']
     
class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.series.slug),slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    article_slug = models.SlugField("Article slug", null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default='')
    notes = HTMLField(blank=True, default='')
    published = models.DateTimeField("Date published", default=timezone.now)
    modified =models.DateTimeField("date modified", default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    publish = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/noimage.jpg',upload_to=image_upload_to, max_length=255)

    def __str__(self): 
        return self.title

    @property
    def slug(self): 
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published','title']

class Contact(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    information = models.TextField()
    reden = models.CharField(max_length=100,choices=REDEN, default="vraag")
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self): 
        return self.firstname + "   " + self.lastname + "__________"+self.reden