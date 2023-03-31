# Generated by Django 4.1.5 on 2023-03-21 10:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_subscribedusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]