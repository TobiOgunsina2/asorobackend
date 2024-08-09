# Generated by Django 5.0.4 on 2024-08-06 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_normalcomponenttype_slide_slidetype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide',
            old_name='Sentence',
            new_name='sentence',
        ),
        migrations.AddField(
            model_name='slide',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.note'),
        ),
    ]
