# Generated by Django 5.0.4 on 2024-08-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_slide_image_slide_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='audio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
