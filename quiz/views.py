from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import(
    Category,
    Quiz,
    Question,
)
from .serializers import(
    CategorySerializer,
    QuizSerializer,
    QuestionSerializer,
)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    # filter kısmı 
    '''
    Bunu bir aşağida get_queryset() methodunu 
    override ederek dinamic url ile de yapabiliriz.
    '''
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category'] # id ile erişim
    # filterset_fields = ['category__name'] # name ile erişim
    search_fields = ['title']


# filtrelemeye alternatif
'''
    get_queryset() methodunu override ederek 
    dinamic url ile filtreleme yapilişi.
''' 
class QuizCategoryList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    def get_queryset(self):
        category=self.kwargs['category']
        name = Category.objects.get(name__iexact=category)
        quiz_category = Quiz.objects.filter(category=name.id)
        return quiz_category
    
    
    
    
class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['quiz', 'difficulty'] # id ile erişim
    filterset_fields = ['quiz__title'] # name ile erişim
    
    
# filtrelemeye alternatif
'''
    get_queryset() methodunu override ederek 
    dinamic url ile filtreleme yapilişi.
''' 
class QuestionQuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        quiz=self.kwargs['quiz']
        title = Quiz.objects.get(title__iexact=quiz)
        quiz_title = Question.objects.filter(quiz_id=title.id)
        return quiz_title




