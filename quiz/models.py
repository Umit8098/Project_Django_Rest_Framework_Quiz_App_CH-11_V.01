from django.db import models

class CreateUpdateDate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category Name')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural ='Categories'
    
    @property
    def quiz_count(self):
        # return self.quiz_set.count() # 1. yöntem. Çalışması için modelde related_name olmamalı!
        return self.quizzes.count() # 2. yöntem. related_name ile çalışan yöntem.
        

class Quiz(CreateUpdateDate):
    title = models.CharField(max_length=50, verbose_name='Quiz Title')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE) # 1. Yöntem için related_name yok.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizzes') # 2. yöntem. related_name var.

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural ='Quizzes'

    @property
    def question_count(self):
        return self.question_set.count() # 1. yöntem.
        # return self.questions.count() # 2. yöntem.

        
class Question(CreateUpdateDate):
    SCALE = (
        ('B', 'Begginer'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    difficulty = models.CharField(max_length=1, choices=SCALE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural ='Questions'

class Option(CreateUpdateDate):
    option_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    is_right = models.BooleanField(default=False)
    is_check = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text
    
    class Meta:
        verbose_name_plural ='Options'