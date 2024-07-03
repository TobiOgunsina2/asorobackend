from django.contrib import admin
from .models import Unit, Lesson, Word, Phrase, Note, Sentence

# Register your models here.

class ObjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Unit, ObjectAdmin)
admin.site.register(Lesson, ObjectAdmin)
admin.site.register(Word, ObjectAdmin)
admin.site.register(Sentence)
admin.site.register(Phrase, ObjectAdmin)
admin.site.register(Note, ObjectAdmin)
