# Generated by Django 5.0.4 on 2024-08-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_slide_slidetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customslide',
            name='normalComponentType',
            field=models.CharField(choices=[('i', 'Intro'), ('m', 'MultipleChoice'), ('y', 'TrueFalse'), ('b', 'BuildBlock'), ('f', 'fill'), ('p', 'MatchPairs'), ('x', 'TextWrite'), ('d', 'Dialogue'), ('n', 'Note')], max_length=1),
        ),
        migrations.AlterField(
            model_name='slide',
            name='slideType',
            field=models.CharField(choices=[('i', 'Intro'), ('m', 'MultipleChoice'), ('y', 'TrueFalse'), ('b', 'BuildBlock'), ('f', 'fill'), ('p', 'MatchPairs'), ('x', 'TextWrite'), ('d', 'Dialogue'), ('n', 'Note')], max_length=1),
        ),
    ]
