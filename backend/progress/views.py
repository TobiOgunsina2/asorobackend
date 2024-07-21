from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .models import Progress, SentenceProgress, PhraseProgress, WordProgress, LessonProgress
from rest_framework.response import Response
from .serializers import ProgressSerializer, SentenceProgressSerializer, WordProgressSerializer, PhraseProgressSerializer, LessonProgressSerializer
from api.models import Phrase, Sentence, Word, Lesson
from datetime import date, timedelta
from django.shortcuts import get_object_or_404
from api.serializers import UserSerializer
# Create your views here.

class GetProfile(APIView):
    def get(self, request, id, *args, **kwargs):
        myuser = get_object_or_404(User, pk=id)

        progress = Progress.objects.get(user=myuser)
        progress_serializer = ProgressSerializer(Progress.objects.get(user=myuser))

        sentences = SentenceProgressSerializer(SentenceProgress.objects.filter(progressObj=progress), many=True).data
        words = WordProgressSerializer(WordProgress.objects.filter(progressObj=progress), many=True).data
        phrases = PhraseProgressSerializer(PhraseProgress.objects.filter(progressObj=progress), many=True).data
        lessons = LessonProgressSerializer(LessonProgress.objects.filter(progressObj=progress.id), many=True).data
        # Create serializers, serialize and add to progress object
        progress_data = progress_serializer.data

        progress_data['sentences'] = sentences
        progress_data['phrases'] = phrases
        progress_data['words'] = words
        progress_data['lessons'] = lessons

        shortened_user = myuser.first_name[0]+myuser.last_name[0]
        serialized = UserSerializer(myuser)
        data = serialized.data
        data['shortened_user']= shortened_user

        finished_data = {'userData': data, 'progressData': progress_data}
        return Response(finished_data)

class UpdateProgress(APIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Progress.objects.get(user=pk)
        except Progress.DoesNotExist:
            raise Progress
    
    def put(self, request, *args, **kwargs):
        progress = self.get_object(request.user.id)
        data = request.data
        
        try:
            lessonQueryset = LessonProgress.objects.filter(lesson__pk=data['lesson'], progressObj=progress)
            lesson = lessonQueryset.first()
            if len(lessonQueryset)==1:
                lesson.completed=True
                lesson.save()
                print('updating')
            else:
                lessonObj = Lesson.objects.filter(id=data['lesson']).first()
                LessonProgress.objects.create(lesson=lessonObj, progressObj=progress, completed=True)
            #lesson = LessonProgress.objects.update_or_create(progressObj=progress, lesson__pk=data['lesson'], defaults={'completed': True})

        except:
            """lessonObj = Lesson.objects.filter(id=data['lesson']).first()
            LessonProgress.objects.create(lesson=lessonObj, progressObj=progress, completed=True)
            print('creating')"""
            pass
        
        for i in data['phrases']:
            try:
                phrase = PhraseProgress.objects.filter(phrase__pk=i, progressObj=progress).first()
                if phrase.masteryLevel<15:
                    phrase.masteryLevel=phrase.masteryLevel+1
                    phrase.save()
            except:
                phraseObj = Phrase.objects.get(pk=i)
                phrase = PhraseProgress.objects.create(phrase=phraseObj, progressObj=progress)
                phrase.save()
        for i in data['sentences']:
            try:
                sentence = SentenceProgress.objects.filter(sentence__pk=i, progressObj=progress).first()
                if sentence.masteryLevel<15:
                    sentence.masteryLevel=sentence.masteryLevel+1
                    sentence.save()
            except:
                sentenceObj = Sentence.objects.filter(id=i).first()
                sentence = SentenceProgress.objects.create(sentence=sentenceObj, progressObj=progress)
                sentence.save()
        for i in data['words']:
            try:
                word = WordProgress.objects.filter(word__pk=i, progressObj=progress).first()
                if word.masteryLevel<15:
                    word.masteryLevel=word.masteryLevel+1
                    word.save()
            except:
                wordObj = Word.objects.filter(id=i).first()
                word = WordProgress.objects.create(word=wordObj, progressObj=progress)
                word.save()
        

        if progress.lastUpdate == date.today():
            pass
        elif progress.lastUpdate == (date.today() - timedelta(days=1)):
            progress.streak= progress.streak+1
            progress.lastUpdate = date.today()
        else:
            progress.streak=1
            progress.lastUpdate = date.today()     
        progress.save()
        serializer = ProgressSerializer(progress)
        return Response(serializer.data)
        
