from django.urls import path
from .views import (
    CategoryList,
    QuizList,
    QuizCategoryList,
    QuestionList,
    QuestionQuizList,
)

urlpatterns = [
    path('', CategoryList.as_view()),
    path('quiz/', QuizList.as_view()),
    path('quiz-category/<str:category>/', QuizCategoryList.as_view()),
    path('question/', QuestionList.as_view()),
    path('question-quiz/<str:quiz>', QuestionQuizList.as_view()),
]
