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
    translation = models.CharField(max_length=100)
    note = models.CharField(max_length=300, blank=True, null=True)
    
    relatedPhrases= models.ManyToManyField('self', blank=True)
    containedWords = models.ManyToManyField(Word)
    # to attach to contained words to show user the parts of the phrase
    brokenDownPhrase = models.CharField(max_length=100, default='', blank=True, null=True)


    def __str__(self):
        return self.text


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    lessonName = models.CharField(max_length=100)
    lessonOrder = models.CharField(max_length=100)
    lessonDescription = models.CharField(max_length=300, default='')
    phrase = models.ManyToManyField(Phrase, default='')
    words = models.ManyToManyField(Word, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.lessonName

slideTypes = {
    'i':'Intro', 
    'm': 'MultipleChoice',
    't': 'TwoMultipleChoice',  
    'y': 'TrueFalse', 
    'b': 'BuildBlock', 
    'f': 'Fill In Blank', 
    'p': 'MatchPairs', 
    'x': 'TextWrite', 
    'd': 'Dialogue',
    'n': 'Note'
}

class CustomSlide(models.Model):
    id = models.AutoField(primary_key=True)
    normalComponentType = models.CharField(max_length=1, choices=slideTypes)
    prompt = models.CharField(max_length=200, default='')
    options = models.CharField(max_length=500, blank=True, null=True) # Format= #E kaale #E kaaro #E kurole # Answer not included
    answer = models.CharField(max_length=300, default='')
    dialogue = models.CharField(max_length=1000, blank=True, null=True) # Format= #Ms. Folake:I know #Seyi: Yes #Ms. Folake: Cool
    audio = models.CharField(max_length=300, default='')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=1)

class Sentence(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100, default="")
    translation = models.CharField(max_length=100, default="")
    note = models.CharField(max_length=300, blank=True, null=True)
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
    note = models.TextField(max_length=1000)
    audio = models.CharField(max_length=300, blank=True, null=True)
    
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title


class Slide(models.Model):
    id = models.AutoField(primary_key=True)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    slideType = models.CharField(max_length=1, choices=slideTypes)
    
    phrase = models.ManyToManyField(Phrase)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, blank=True, null=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)

    prompt = models.CharField(max_length=200, default='', blank=True, null=True)
    options = models.CharField(max_length=500, blank=True, null=True) # Format= #E kaale #E kaaro #E kurole # Answer not included
    answer = models.CharField(max_length=300, default='', blank=True, null=True)
    dialogue = models.CharField(max_length=1000, blank=True, null=True) # Format= #Ms. Folake:I know #Seyi: Yes #Ms. Folake: Cool
    audio = models.CharField(max_length=300, default='', blank=True, null=True)
    video = models.CharField(max_length=50, default='', blank=True, null=True)
    image = models.CharField(max_length=300, default='', blank=True, null=True)

    def __str__(self):
        word = ''
        audio = ''
        if self.phrase.all().first():
            word=self.phrase.all().first().text
        if str(self.audio) != 'None':
            audio = str(self.audio)
        return str(self.lesson)[:4]+' '+word+' '+slideTypes[self.slideType]+ ' ' + audio
