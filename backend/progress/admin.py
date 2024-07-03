from django.contrib import admin
from .models import Progress, PhraseProgress, SentenceProgress, WordProgress, LessonProgress

# Register your models here.

admin.site.register(Progress)
admin.site.register(PhraseProgress)
admin.site.register(SentenceProgress)
admin.site.register(WordProgress)
admin.site.register(LessonProgress)


