from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    
from api.models import Phrase, Sentence, Word, Lesson

# Create your models here.

class Progress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    streak = models.IntegerField(default=0)
    lastUpdate = models.DateField(blank=True, default=datetime.now)
    lastLesson = models.ForeignKey(Lesson, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class WordProgress(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    masteryLevel = IntegerRangeField(min_value=0, max_value=4, default=0, null=True)
    progressObj = models.ForeignKey(Progress, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.word)

class PhraseProgress(models.Model):
    id = models.AutoField(primary_key=True)
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE)
    masteryLevel = IntegerRangeField(min_value=0, max_value=6, default=0, null=True)
    progressObj = models.ForeignKey(Progress, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.phrase)

class SentenceProgress(models.Model):
    id = models.AutoField(primary_key=True)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    masteryLevel = IntegerRangeField(min_value=0, max_value=6, default=0, null=True)
    progressObj = models.ForeignKey(Progress, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.sentence)
    
class LessonProgress(models.Model):
    id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    progressObj = models.ForeignKey(Progress, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.lesson)
