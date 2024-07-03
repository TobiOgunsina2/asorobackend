from rest_framework import serializers
from .models import Progress, PhraseProgress, SentenceProgress, LessonProgress, WordProgress
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'user', 'streak', 'lastLesson']

class WordProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordProgress
        fields = ['id', 'word', 'masteryLevel', 'progressObj']


class PhraseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhraseProgress
        fields = ['id', 'phrase', 'masteryLevel', 'progressObj']

class SentenceProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentenceProgress
        fields = ['id', 'sentence', 'masteryLevel', 'progressObj']

class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = ['id', 'lesson', 'completed', 'progressObj']


