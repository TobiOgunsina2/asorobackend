from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, LessonSerializer, LessonUnitSerializer, UnitSerializer, MyTokenObtainPairSerializer, PhraseSerializer, SentenceSerializer, RegisterSerializer, NoteSerializer, SlideSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Word, Unit, Lesson,Phrase, Sentence, Slide, Note
from progress.models import Progress, PhraseProgress, SentenceProgress, LessonProgress
from progress.serializers import LessonProgressSerializer, ProgressSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from datetime import date, timedelta


# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class GetLesson(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated] # Change to IsAuthenticated

    def list(self, request, uid, lid):
        queryset = self.get_queryset().filter(unit=Unit.objects.get(id=uid).id).filter(id=lid)
        serializer = LessonSerializer(queryset, many=True)
        """serializer.data[0]['phrases'] = []
        for i in serializer.data[0]['phrase']:
            serializer.data[0]['phrases'] += PhraseSerializer(Phrase.objects.filter(id=i), many=True).data
            for x in range(len(serializer.data[0]['phrases'][-1]['relatedPhrases'])):
                serializer.data[0]['phrases'][-1]['relatedPhrases'][x-1] = PhraseSerializer(Phrase.objects.get(id=serializer.data[0]['phrases'][-1]['relatedPhrases'][x-1])).data
            for x in range(len(serializer.data[0]['phrases'][-1]['containedWords'])):
                w = Word.objects.get(id=serializer.data[0]['phrases'][-1]['containedWords'][x-1])
                serializer.data[0]['phrases'][-1]['containedWords'][x-1] = WordSerializer(Word.objects.get(id=serializer.data[0]['phrases'][-1]['containedWords'][x-1])).data
                print(w, i)"""
        serializer.data[0]['slides'] = SlideSerializer(Slide.objects.filter(lesson=lid), many=True).data

        return Response(serializer.data)

class GetReview(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, id):
        progress = Progress.objects.get(user=id)
        phrase_progress = PhraseProgress.objects.filter(progressObj=progress)
        sentence_progress =SentenceProgress.objects.filter(progressObj=progress)
        phrases = []
        sentences = []
        for i in phrase_progress:
            phrase_data = PhraseSerializer(Phrase.objects.filter(id=i.phrase.id), many=True).data
            phrase_data[0]['masteryLevel'] = i.masteryLevel
            phrases+=phrase_data
        for i in sentence_progress:
            sentence_data = SentenceSerializer(Sentence.objects.filter(id=i.sentence.id), many=True).data
            sentence_data[0]['masteryLevel'] = i.masteryLevel 
            sentences+=sentence_data
        serializer = {'data': {'phrases': phrases, 'sentences': sentences}}

        return Response(serializer['data'])

class UnitList(generics.ListAPIView):
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]# Change to IsAuthenticated
    queryset = Unit.objects.all()

    def list(self, request, id):
        queryset = self.get_queryset()

        myuser = get_object_or_404(User, pk=id)

        progress = Progress.objects.get(user=myuser)
            
        serializer = UnitSerializer(queryset, many=True)
        completed_lessons = LessonProgressSerializer(LessonProgress.objects.filter(progressObj=progress.id), many=True).data
        
        if progress.lastUpdate == date.today():
            pass
        elif progress.lastUpdate > (date.today() - timedelta(days=2)):
            progress.streak = 0
        progress.lastUpdate = date.today()
        progress.save()

        serializedProgress=ProgressSerializer(progress)

        # Return Unit with Lesson Names and ids
        for i in range(len(serializer.data)):
            serializer.data[i]['lessons'] = LessonUnitSerializer(Lesson.objects.filter(unit=serializer.data[i]['id']), many=True).data
        return Response({'data': serializer.data, 'completedLessons': completed_lessons, 'lastLesson': serializedProgress.data['lastLesson']})

class GetPhrase(generics.ListAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
    permission_classes = [AllowAny] # Change to IsAuthenticated

    def list(self, request, pk):
        queryset = self.get_queryset().filter(id=pk)
        serializer = PhraseSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateUserView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request,  *args, **kwargs):
        serialized = RegisterSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        user = serialized.save()
        progress = Progress.objects.create(user=user)
        progress.save()
        refresh = RefreshToken.for_user(user)
        response = {
            'success': True,
            'user': serialized.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(response)