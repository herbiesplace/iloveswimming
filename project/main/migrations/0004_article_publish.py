# Generated by Django 4.1.5 on 2023-02-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_article_notes_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]