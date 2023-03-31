from django.db import models
from django.utils import timezone

 
class InteresanteLink(models.Model):
    titel = models.CharField(max_length=200)
    beschrijving = models.TextField()
    link = models.URLField()
    gepubliceerd = models.DateTimeField("Datum gepubliceerd", default=timezone.now)

    def __str__(self): 
        return self.titel

    class Meta:
        ordering = ['-gepubliceerd']