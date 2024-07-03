# Generated by Django 5.0.4 on 2024-06-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(default='', max_length=100)),
                ('sentenceTranslation', models.CharField(default='', max_length=100)),
                ('sentenceNote', models.CharField(blank=True, max_length=300, null=True)),
                ('brokenDownSentence', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('containedPhrases', models.ManyToManyField(blank=True, null=True, to='api.phrase')),
            ],
        ),
    ]