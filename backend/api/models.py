from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Unit(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    unitName = models.CharField(max_length=100)
    unitDescription = models.CharField(max_length=100)

    def __str__(self):
        return self.unitName


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100)
    wordTranslation = models.CharField(max_length=100)
    wordNote = models.CharField(max_length=300, blank=True, null=True)
    relatedWords= models.ManyToManyField('self',blank=True)
    
    def __str__(self):
        return self.text


class Phrase(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100)
    phraseTranslation = models.CharField(max_length=100)
    phraseNote = models.CharField(max_length=300, blank=True, null=True)

    
    relatedPhrases= models.ManyToManyField('self', blank=True)
    containedWords = models.ManyToManyField(Word)
    # to attach to contained words to show user the parts of the phrase
    brokenDownPhrase = models.CharField(max_length=100, default='', blank=True, null=True)


    def __str__(self):
        return self.text



class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    lessonName = models.CharField(max_length=100)
    lessonType = models.CharField(max_length=100)
    lessonDescription = models.CharField(max_length=300, default='')
    phrase = models.ManyToManyField(Phrase, default='')
    words = models.ManyToManyField(Word, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.lessonName

class Sentence(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100, default="")
    sentenceTranslation = models.CharField(max_length=100, default="")
    sentenceNote = models.CharField(max_length=300, blank=True, null=True)
    containedPhrases = models.ManyToManyField(Phrase, blank=True)
    containedWords = models.ManyToManyField(Word, blank=True)
    order = models.CharField(max_length=100, default="")

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    # to attach to contained words to show user the parts of the phrase
    brokenDownSentence = models.CharField(max_length=100, default='', blank=True, null=True)


    def __str__(self):
        return self.text


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    note = models.CharField(max_length=100)
    
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title




