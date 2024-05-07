from django.contrib import admin
import nested_admin
from .models import (
    Category,
    Quiz,
    Question,
    Option,
)

class OptionAdmin(nested_admin.NestedTabularInline):
    model = Option
    extra = 5 # Sayfada kaçtane görünsün? default 3'tür.
    max_num = 4 # maximum 4 adet olabilir.

class QuestionAdmin(nested_admin.NestedTabularInline):
    model = Question
    inlines = [OptionAdmin]
    extra = 4 
    max_num = 4 

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionAdmin]

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Option)