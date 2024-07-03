from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, LessonSerializer, UnitSerializer, WordSerializer, MyTokenObtainPairSerializer, PhraseSerializer, SentenceSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Word, Unit, Lesson,Phrase, Sentence
from progress.models import Progress, PhraseProgress, SentenceProgress
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class GetLesson(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny] # Change to IsAuthenticated

    def list(self, request, uid, lid):
        queryset = self.get_queryset().filter(unit=Unit.objects.get(id=uid).id).filter(id=lid)
        serializer = LessonSerializer(queryset, many=True)
        serializer.data[0]['phrases'] = []
        for i in serializer.data[0]['phrase']:
            serializer.data[0]['phrases'] += PhraseSerializer(Phrase.objects.filter(id=i), many=True).data
            for x in range(len(serializer.data[0]['phrases'][-1]['relatedPhrases'])):
                serializer.data[0]['phrases'][-1]['relatedPhrases'][x-1] = PhraseSerializer(Phrase.objects.get(id=serializer.data[0]['phrases'][-1]['relatedPhrases'][x-1])).data
        serializer.data[0]['sentences'] = SentenceSerializer(Sentence.objects.filter(lesson=lid), many=True).data
        return Response(serializer.data)

class GetReview(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        progress = Progress.objects.get(user=request.user.id)
        phrase_progress = PhraseProgress.objects.filter(progressObj=progress)
        sentence_progress =SentenceProgress.objects.filter(progressObj=progress)
        phrases = []
        sentences = []
        for i in phrase_progress:
            phrases+=PhraseSerializer(Phrase.objects.filter(id=i.phrase.id), many=True).data
        for i in sentence_progress:
            sentences+=SentenceSerializer(Sentence.objects.filter(id=i.sentence.id), many=True).data
        serializer = {'data': {'phrases': phrases, 'sentences': sentences}}

        return Response(serializer['data'])

class UnitList(generics.ListAPIView):
    serializer_class = UnitSerializer
    permission_classes = [AllowAny]# Change to IsAuthenticated
    queryset = Unit.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
            
        serializer = UnitSerializer(queryset, many=True)
        # Return Unit with Lesson Names and ids
        for i in range(len(serializer.data)):
            serializer.data[i]['lessons'] = LessonSerializer(Lesson.objects.filter(unit=serializer.data[i]['id']), many=True).data
        return Response(serializer.data)

class GetPhrase(generics.ListAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
    permission_classes = [AllowAny] # Change to IsAuthenticated

    def list(self, request, pk):
        queryset = self.get_queryset().filter(id=pk)
        serializer = PhraseSerializer(queryset, many=True)
        print(serializer.data)
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
        print(Token.objects.get_or_create(user=user)[0].generate_key())
        refresh = RefreshToken.for_user(user)
        response = {
            'success': True,
            'user': serialized.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
        return Response(response)



