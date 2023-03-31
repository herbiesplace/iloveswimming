from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
# ivm image
from django.template.defaultfilters import slugify
from django.utils import timezone
import os

class CustomUser(AbstractUser):
    STATUS= (
        ('regular', 'regular'),
        ('subscriber','subscriber'),
        ('moderator','moderator')
    )
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", instance)
        return None

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField('Description', max_length=600, default='', blank=True)
    image = models.ImageField(default='default/avatar.png',upload_to=image_upload_to)
    follows = models.ManyToManyField("self",related_name="followed_by", symmetrical=False,blank=True)

    def __str__(self): 
        return self.username

class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self): 
        return self.email

def followitself(sender, instance, created, **kwargs):
    if created:
        it_self = CustomUser(user=instance)
        it_self.save()
        it_self.follows.set([instance.username.id])

post_save.connect(followitself, sender=AbstractUser)