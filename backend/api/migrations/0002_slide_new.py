# Generated by Django 5.0.4 on 2024-10-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='new',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]