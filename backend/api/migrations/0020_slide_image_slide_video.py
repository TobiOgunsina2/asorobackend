# Generated by Django 5.0.4 on 2024-08-07 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_remove_customslide_lesson_alter_slide_lesson_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='video',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]