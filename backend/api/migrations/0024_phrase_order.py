# Generated by Django 5.0.4 on 2024-09-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_rename_wordnote_word_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrase',
            name='order',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
