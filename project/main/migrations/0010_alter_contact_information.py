# Generated by Django 4.1.5 on 2023-03-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_contact_reden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='information',
            field=models.TextField(),
        ),
    ]