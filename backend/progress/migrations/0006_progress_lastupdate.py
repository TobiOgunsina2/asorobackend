# Generated by Django 5.0.4 on 2024-06-25 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0005_alter_sentenceprogress_masterylevel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='lastUpdate',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
