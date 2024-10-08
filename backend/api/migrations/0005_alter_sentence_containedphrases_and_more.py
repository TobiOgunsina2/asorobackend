# Generated by Django 5.0.4 on 2024-06-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_sentence_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='containedPhrases',
            field=models.ManyToManyField(blank=True, to='api.phrase'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='containedWords',
            field=models.ManyToManyField(blank=True, to='api.word'),
        ),
    ]
