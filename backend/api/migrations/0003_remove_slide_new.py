# Generated by Django 5.0.4 on 2024-10-06 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_slide_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='new',
        ),
    ]