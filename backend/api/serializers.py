from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Word, Unit, Lesson, Phrase, Sentence, Note, CustomSlide, Slide
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {"password": {"write_only": True}}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'text', 'wordTranslation', 'wordNote', 'relatedWords']

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['id', 'text', 'translation', 'sentenceNote','lesson', 'order', 'containedPhrases', 'containedWords', 'brokenDownSentence']
class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['id', 'text', 'translation', 'phraseNote', 'relatedPhrases', 'containedWords', 'brokenDownPhrase']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'note', 'lesson']

class CustomSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomSlide
        fields = ['id', 'normalComponentType', 'prompt', 'options', 'answer', 'dialogue', 'lesson']

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ['id', 'lesson', 'slideType', 'phrase', 'sentence', 'note', 'prompt', 'options', 'answer', 'dialogue', 'image','audio', 'video']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'lessonName', 'phrase', 'lessonDescription', 'lessonOrder', 'unit']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'unitName', 'unitDescription']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add your extra responses here
        data['user'] = self.user.pk
        return data
