# Generated by Django 4.1.5 on 2023-03-24 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=200)),
                ('beschrijving', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='video/%y')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]