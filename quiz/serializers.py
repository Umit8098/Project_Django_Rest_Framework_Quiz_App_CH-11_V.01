from rest_framework import serializers
from .models import (
    Category,
    Quiz,
    Option,
    Question,
)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'quiz_count',
        )

class QuizSerializer(serializers.ModelSerializer):
    
    category = serializers.StringRelatedField()
    
    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question_count',
        )


class OptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Option
        fields = (
            'id',
            'option_text',
            # 'question',
            'is_right',
            'is_check',
        )

        
class QuestionSerializer(serializers.ModelSerializer):
    
    options = OptionSerializer(many=True) # 'options' -> Option modeldeki Question modeline ForeingKey ile bağlı field'a tanımlı related_name!
    quiz = serializers.StringRelatedField()
    quiz_id = serializers.IntegerField()
    
    class Meta:
        model = Question
        fields = (
            'id',
            'quiz',
            'quiz_id',
            'title',
            'options',
            'difficulty',
        )

