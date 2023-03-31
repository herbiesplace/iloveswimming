# Generated by Django 4.1.5 on 2023-02-28 16:14

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default/avatar.png', upload_to=users.models.CustomUser.image_upload_to),
        ),
    ]
