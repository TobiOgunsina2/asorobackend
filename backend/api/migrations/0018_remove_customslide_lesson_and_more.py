# Generated by Django 5.0.4 on 2024-08-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_customslide_normalcomponenttype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customslide',
            name='lesson',
        ),
        migrations.AlterField(
            model_name='customslide',
            name='normalComponentType',
            field=models.CharField(choices=[('i', 'Intro'), ('m', 'MultipleChoice'), ('t', 'TwoMultipleChoice'), ('y', 'TrueFalse'), ('b', 'BuildBlock'), ('f', 'Fill In Blank'), ('p', 'MatchPairs'), ('x', 'TextWrite'), ('d', 'Dialogue'), ('n', 'Note')], max_length=1),
        ),
        migrations.AlterField(
            model_name='slide',
            name='slideType',
            field=models.CharField(choices=[('i', 'Intro'), ('m', 'MultipleChoice'), ('t', 'TwoMultipleChoice'), ('y', 'TrueFalse'), ('b', 'BuildBlock'), ('f', 'Fill In Blank'), ('p', 'MatchPairs'), ('x', 'TextWrite'), ('d', 'Dialogue'), ('n', 'Note')], max_length=1),
        ),
        migrations.AddField(
            model_name='customslide',
            name='lesson',
            field=models.ManyToManyField(default=1, to='api.lesson'),
        ),
    ]
