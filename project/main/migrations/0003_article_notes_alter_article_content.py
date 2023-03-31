# Generated by Django 4.1.5 on 2023-01-31 14:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
    ]
