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
        fields = ['id', 'text', 'translation', 'note', 'relatedWords']

class PhraseSerializer(serializers.ModelSerializer):
    containedWords = WordSerializer(many=True, read_only=True)
    class Meta:
        model = Phrase
        fields = ['id', 'text', 'translation', 'note', 'relatedPhrases', 'containedWords', 'brokenDownPhrase']

class SentenceSerializer(serializers.ModelSerializer):
    containedPhrases = PhraseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Sentence
        fields = ['id', 'text', 'translation', 'note', 'lesson', 'order', 'containedPhrases', 'containedWords', 'brokenDownSentence']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'note', 'audio','lesson']

class CustomSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomSlide
        fields = ['id', 'normalComponentType', 'prompt', 'options', 'answer', 'dialogue', 'lesson']

class SlideSerializer(serializers.ModelSerializer):
    phrase = PhraseSerializer(many=True, read_only=True)
    sentence = SentenceSerializer(read_only=True)
    class Meta:
        model = Slide
        fields = ['id', 'lesson', 'slideType', 'phrase', 'sentence', 'note', 'prompt', 'options', 'answer', 'dialogue', 'image','audio', 'video']


class LessonSerializer(serializers.ModelSerializer):
    sentences = SentenceSerializer(many=True, read_only=True)
    phrase = PhraseSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ['id', 'lessonName', 'phrase', 'sentences','lessonDescription', 'lessonOrder', 'unit']


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
