# Generated by Django 5.0.4 on 2024-08-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_customslide_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='customslide',
            name='audio',
            field=models.CharField(default='', max_length=300),
        ),
    ]