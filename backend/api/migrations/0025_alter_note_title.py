# Generated by Django 5.0.4 on 2024-09-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_phrase_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]