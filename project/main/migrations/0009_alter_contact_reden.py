# Generated by Django 4.1.5 on 2023-03-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='reden',
            field=models.CharField(choices=[('vraag', 'vraag'), ('opmerking', 'opmerking'), ('suggestie', 'suggestie'), ('probleem', 'probleem')], default='vraag', max_length=100),
        ),
    ]
