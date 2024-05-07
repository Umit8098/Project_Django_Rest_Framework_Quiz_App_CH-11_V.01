## Project Quiz App

### Quiz App

- Projenin genel görünümü Quiz_App.jpg de gösterilmiştir.
  
```bash
- py -m venv env
# - python3.10 -m venv env
- ./env/Scripts/activate
- pip install djangorestframework
- pip install python-decouple
- pip freeze > requirements.txt
- # pip install -r requirements.txt
- django-admin startproject main .
```


- go to settings.py and add rest_framework;

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    # my_apps
    
    # 3rd_party_packages
    'rest_framework',
]
```

- create .env and .gitignore files, hidden to SECRET_KEY.
  
- Create .env file on root directory. We will collect our variables in this file.
- 
```py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

```py
SECRET_KEY = o5o9...
```

- create app

```powershell
- py manage.py startapp quiz
```

- go to settings.py and add our app;

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    # my_apps
    'quiz',
    # drf
    'rest_framework',
]
```

- Migrate dbs:
```powershell
- python manage.py migrate
- py manage.py runserver
```

- Create superuser:
```powershell
- python manage.py createsuperuser
```

- Backend yazıyorsak bir application a ait db de birşeyler tutmak istiyoruzdur. Backend aslında db işlemleri, CRUD işlemleridir. db siz backend olmaz, relational olur non-relational olur farketmez, db de data tutacağımız anlamına gelir. Onun için ilk iş tabloları/modelleri ve relational ları belirlemektir.
- Quiz app imizde modellerimizi oluşturuyoruz;

models.py
```py
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

class Quiz(CreateUpdateDate):
    title = models.CharField(max_length=50, verbose_name='Quiz Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural ='Quizzes'
        
class Question(CreateUpdateDate):
    SCALE = (
        ('B', 'Begginer'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    defficulty = models.CharField(max_length=1, choices=SCALE)

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
```

- Oluşturduğumuz modellerimizi admin panelde görmek için admin.py da register ediyoruz.

admin.py 
```py
from django.contrib import admin
from .models import (
    Category,
    Quiz,
    Question,
    Option,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
```

```powershell
- python manage.py makemigrations
- python manage.py migrate
- py manage.py runserver
```

#### django-nested-admin package

- Normalde admin panelde ilişkili tablolara veri girişi yapmak için her bir tabloya ayrı ayrı veri girdikten sonra ilişkili olduğu tabloya veri girebiliyoruz.
- Ancak ilişkili tabloları, birbiri içerisine nested şekilde göstererek tek bir ekrandan ilişkili tüm tablolara veri girişi yapabilmek için;  
- Quiz in altında Question, onun da altında Options tablolarına aynı ekrandan veri girişi yapabilmek için; 
- Yani tek seferde hepsini create edebilmek için;
- https://django-nested-admin.readthedocs.io/en/latest/quickstart.html
- django-nested-admin isimli 3rd party package ile bunu yapabiliyoruz.

terminal
```bash
- pip install django-nested-admin
- pip freeze > requirements.txt
```

- go to settings.py and add our django-nested-admin 3rd party package to INSTALLED_APPS;

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    # my_apps
    'quiz',
    # drf
    'rest_framework',
    # third party packages
    'nested_admin',
]
```

Add URL-patterns:

urls.py
```py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
]
```

- Eski django versionlarında url(r'^_neste...) (r=regular expression) şeklindeki yapı artık kullanılmıyor. Python3 ile artık  url path'i normal path('.../', ...) şeklinde belirtiliyor.
  
url(r'^_nested_admin/', include('nested_admin.urls')),


- django-nested-admin paketini admin panelde kullanacağız. Bunun için admin.py da birtakım ayarlar yapıyoruz. Öncelikle nested_admin paketini import ediyoruz.
  import nested_admin
- Sonrasında neyi neyin içerisine koyacağız ona bakıyoruz. 
- En içte options (şıklarımız, seçeneklerimiz) larımız olacak.
- options ları questions ların içine, questions ları da quiz lerin içine koyacağız. Böylelikle quiz içinde question, onun da içinde option olmak üzere hepsine tek bir arayüzden erişim sağlayabileceğiz.

admin.py
```py
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
    max_num = 7 # maximum 7 adet olabilir.


class QuestionAdmin(nested_admin.NestedTabularInline):
    model = Question
    inlines = [OptionAdmin]
    extra = 5 
    max_num = 20


class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionAdmin]

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Option)
```

- Test ediyoruz. Admin panele gittiğimizde Quiz tablosunda creation işlemi yaparken aşağıya doğru ilişkili olduğu tablolarda creation işlemlerini de aynı sayfada yapabilme imkanı sağladığını gördük.
- Bunu nasıl kullanabiliriz; Mesela bir teacher grubu oluşturup, CRUD yetkisi veririz.

#### API ->

- Kullanıcılar için Category leri listeleyip, bunlar içinden category seçip, ardından da bu category'ye ait quizlere erişebilmesi için view imizi yazıyoruz. Burada kullanıcılar için sadece GET methodu ile categoryleri listelenip görmesini yeterli görüyoruz.
- Bunun için view imizi generics lerden ListAPIView den inherit ederek oluşturuyoruz.
- Tabi önce Category viewimizin kullanacağı CategorySerializer serializer ını oluşturuyoruz; quiz app imizin içinde serializers.py isminde file oluşturup; 

quiz/serializers.py
```py 
from rest_framework import serializers
from .models import (
    Category,
)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )
    
```

quiz/views.py
```py 
from django.shortcuts import render
from rest_framework import generics
from .models import(
    Category,
)
from .serializers import(
    CategorySerializer,
)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
``` 

##### Modelde ekstra field/property/method yazımı:
- Bu işlem serializersda (MethodField) da yapılabilir. 
- Ayrıca her category içinde kaç adet quiz olduğunu da kullanıcıya models.py da Category modelinin içinde bir method yazarak @property ile sanki modelin yeni bir field ıymış gibi kullanıcıya gösterebiliriz.
- Bunun için Category modelimize gidip; methodumuzu yazıyoruz;
- Burada parent modelimizden child modelimize ulaşmaya çalışıyoruz. Bunun iki yöntemi var;
  - 1- Child modelin isminin küçük harfle yazımı ve _set (quiz_set)
  https://docs.djangoproject.com/en/5.0/topics/db/queries/

  Bu yöntem kullanılacak ise eğer child modelde ilişkili fieldda related_name tanımlaması olmamalıdır. Eğer related name var ise bu yöntem çalışmaz.

  - 2- Child modelde, parent model ile ilişki kurduğumuz field'a related_name isminde bir değişkenle isim verip bu isimle child modelin tüm fieldlarına erişebiliriz. Eğer related_name kullanacaksak terminalde makemigrations ve migrate yapmamız gerekiyor.

- Bir methodu modelin bir attribute'ü, property'si gibi kullanmak için methodun hemen üzerine @property yazarız. Yazmasakda çalışır ama yazarsak daha iyi olur.

- Normalde bir objenin methoduna şu şekilde ulaşırız;
    obj.title          modelin bir attribut'üne ulaşmak  
    obj.quiz_count()   modelin bir methodun sonunda parantez olur.
  Ancak @property yazarak
    obj.quiz_count     şeklinde de ulaşabiliriz.
    obj.title          modelin bir attribut'üne ulaşmak
- Category modelimizde yazdığımız methodun hemen üzerine @property yazarak oluşturduğumuz methodun, modelimizin bir fieldıymış gibi davranmasını sağlayabiliriz. (@property yazmasak da oluyormuş ama garanti olsun yazalım.)
- Bu method bize "..... categorysine bağlı 8 tane quiz var." bunu verecek.

quiz/models.py
```py 
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

```

- Modelimizde ekstra bir field oluşturduk. Bunu serializers'da belirterek API de JSON formatında kullanabiliriz.

quiz/serializers.py
```py 
from rest_framework import serializers
from .models import (
    Category,
)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'quiz_count',
        )
    
```

- Yazdığımız view imizin url'ini oluşturalım.

main/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('quiz/', include('quiz.urls')),
]
```

quiz/urls.py
```py
from django.urls import path
from .views import (
    CategoryList,
)

urlpatterns = [
    path('', CategoryList.as_view()),
]
```


- Şimdi sıra diğer modellerimizin serializer-view-url lerini tanımlamada;

- Quiz modelimizin serializer-view-url' ini yazalım. Burada yine bir count() methodu yazalım modelimizde.

quiz/models.py
```py
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
    defficulty = models.CharField(max_length=1, choices=SCALE)
```

- serializer
  
quiz/serializers.py
```py
from .models import (
    Quiz,
)

class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question_count',
        )

```

- view

quiz/views.py
```py
from .models import(
    Quiz,
)
from .serializers import(
    QuizSerializer,
)

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
```

- url

quiz/urls.py
```py
from .views import (
    QuizList,
)

urlpatterns = [
    path('quiz/', QuizList.as_view()),
]
```

- Burada QuizList viewimizde, category fieldında, parent modeldeki (Category) objelerin id leri görünüyor. Bu viewimiz zaten ListView yani sadece GET ile çalışıyor, POST/PUT/DELLETE/UPDATE yapmıyor. O zaman burada id leri değil de Category modelindeki str methodunda belirtilen şekilde görünsün istiyoruz. Bunu da seializers.py da ilgili serializerda StringRelatedField olarak düzenleyebiliyoruz.  

- serializer
  
quiz/serializers.py
```py
from .models import (
    Quiz,
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

```

#### django-filters package

##### filters

- Bu aşamada category ler arasında filtreleme yapacağız. Yani categoty ler arasından sadece Backend yada Frontend olanlar gelsin istiyoruz.
- Bunu views.py da CategoryList view inde get_queryset() methodunu override ederek de yapabilirdik. (Biraz aşağıda yapılmış hali var.)
- Biz django-filters package ile daha kolay birşekilde yapacağız.
- Bu package vasıtasıyla view'imizde istediğimiz field'a göre filtreleme yap diyebiliyoruz.

```bash
- pip install django-filter
- pip freeze > requirements.txt
```

settings.py
```py
INSTALLED_APPS = [
    # third party packages
    'django_filters',
]

```

- views.py da import ediyoruz. 
- Hangi view imizde kullanacaksak orada filter_backend fieldına tanımlıyoruz.
    filter_backends = [DjangoFilterBackend]
- Bir de hangi field ımıza göre filtreleyeceksek o fieldımızı belirtiyoruz.
    filterset_fields = ['category']
- Artık bizim category fieldımıza göre bir filtremiz oldu.


quiz/views.py
```py
from django_filters.rest_framework import DjangoFilterBackend

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category'] # id ile erişim
```

- Artık kullanıcı ana sayfadan Backend'e bastığı zaman kullanıcıyı şı API'ye yönlendireceğiz.
    http://127.0.0.1:8000/quiz/quiz/?category=1

- Burada category=1 diyoruz, id belirtiyoruz,
- 1 yerine category=django şeklinde de yapabiliriz.

- parent'tan child'a 
     ya related name 
     yada lowercase modelname_set ile ulaşıyoruz. 

- child'dan parent'a ise ilişkili olduğu field__field ile parent'ın istediğimiz fieldına ulaşabiliriz.
     category__name 

quiz/views.py
```py
from django_filters.rest_framework import DjangoFilterBackend

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']
    filterset_fields = ['category__name'] # name ile erişim
```

- Bunun şeklini artık Frontend ile konuşup onlar nasıl isterse (id veya name) ona göre ayarlamak gerekiyor.

##### get_queryset() methodunu override ederek filtreleme;

quiz/views.py
```py
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
```

quiz/urls.py
```py
from .views import (
    QuizCategoryList,
)
urlpatterns = [
    path('quiz-category/<str:category>/', QuizCategoryList.as_view()),
]
```


##### search

- rest_framework ün kendi filters paketinden yapıyoruz bunu.

quiz/views.py
```py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category'] # id ile erişim
    search_fields = ['title']
```


- Artık kullanıcı şu endpointten şu şekilde istek ataraksearch yapabilecek.
  
    http://127.0.0.1:8000/quiz/quiz/?search=angu

- Yine bunu da frontend bizim sunduğumuz endpointe istek atarak search yapabilecek.



##### nested view
- Question modelimizin serializer-view-url' ini yazalım. 
- Bu view imiz nested bir view olacak. Çünkü question text inin altında options/şık lar olacak.
- Böyle olacağı için serializer yazarken önce Option modeleli için bir serializer yazıp daha sonra onun altına Question modeli için bir serializer yazacağız. Böylelikle önce Option için bir serializer oluşup, bu option serialier verilerini de Question serializer içinde göstereceğiz.

- serializers
  
quiz/serializers.py
```py
from .models import (
    Option,
    Question,
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
```

- views

quiz/views.py
```py
from .models import(
    Question,
)
from .serializers import(
    QuestionSerializer,
)

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

```

- urls

quiz/urls.py
```py
from .views import (
    QuestionList,
)

urlpatterns = [
    path('question/', QuestionList.as_view()),
]
```

- Test ediyoruz. Çalışıyor fakat tüm categorylerdeki tüm soruları ve soruların option larını aynı anda görüyoruz. 
  
- filtre koyma;
- Ancak bizim istediğimiz hangi quiz istiyorsak o quizin soruları gelsin.
- Bunun için QuizList view de olduğu gibi bir filtre koyabiliriz.

quiz/views.py
```py
class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['quiz', 'difficulty'] # id ile erişim
    # filterset_fields = ['quiz__title'] # name ile erişim
```


### Authentication (User) App
----------------------------------------------------
##### Buradan başlayarak işaretli kısma kadar kadar standart bir authentication app
(models.py daki Profile modeli opsiyonel, her projeye uymayabilir.)

#### registration, login, logout

- registration, login, logout işlemleri için yeni bir app oluşturacağız.

- users app i oluştur,
 
```powershell
- py manage.py startapp users
```

- INSTALLED_APPS ' e ekle,
settings.py
```py
INSTALLED_APPS = [
    ...
    # may apps
    'quiz',
    'users',
]
```

- settings.py 'a TokenAuthentication ekle
settings.py
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

- dj-rest-auth  paketini yükle
  
https://pypi.org/project/dj-rest-auth/

```powershell
- pip install dj-rest-auth
# dj-rest-auth paketinin versiyonuna dikkat! eski versiyon ile hata verebilir.
- pip freeze > requirements.txt
```

- INSTALLED_APPS 'e 'rest_framework.authtoken' ve 'dj_rest_auth' paketini ekle.
settings.py
```py
INSTALLED_APPS = [
    ...
    # 3rd party packages
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    # may apps
    'quiz',
    'users',
]
```

- migrate
```powershell
- py manage.py migrate
```

- urls configürasyonu yap,

main/urls.py
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('quiz/', include('quiz.urls')),
    path('users/', include('users.urls')),
] 
```

- create users/urls.py ve dj_rest_auth paketinin path ini ekliyoruz.->
users/urls.py
- url pathern ' dj_rest_auth endpointini ekle
```py
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
```

- users app ini oluşturduktan sonra, global olarak TokenAuthentication ayarladık, users ve auth_token ı installed apps e ekledik, urls configürasyonunu yaptık ve django rest auth un bize verdiği endpointleri kurduk/gördük.

- Userlar için djangoun default User medelini kullanacağız.
- Ancak biz oluşturulan userların birer Profile'ı olsun istiyoruz. Userlar için oluşturacağımız Profile modelini djangoun default User modeli ile OneToOneField ilişki kurarak, default User modelinin fieldlarına ek olarak image ve about diye fieldları da ekleyeceğiz.
- users app inin içinde model.py 'a gidip, Profile modelimizi oluşturuyoruz,

users/models.py
```py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(upload_to='images',default='avatar.png', height_field=None, width_field=None, max_length=None)
    about = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    def __str__(self):
        # return self.user.username
        # return self.user.first_name
        return f'{self.user.username} - {self.user.first_name}'
```

- modelde image field kullandığımız için Pillow package kurulumu istedi.install ediyoruz.

```powershell
- pip install Pillow
- pip freeze > requirements.txt
- py manage.py makemigrations
- py manage.py migrate
```

- admin.py da modelimizi register ediyoruz.

```py
from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.register(Profile)
```

#### static/media settings 

- static files -> development ortamında static file ları görebilmek için settings.py ve urls.py da yapmamız gereken ayarlar.

https://docs.djangoproject.com/en/4.2/howto/static-files/


main/urls.py ->
```py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('...', .....),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- settings.py ->
```py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
```

#### registration 

- Şu an için dj_rest_auth un sunduğu login, logout, password_change, password_reset imiz var. Registration ı kendimiz yazacağız. Burada ya register serializer yada Profile serializer yazacağız. Biz RegisterSerializer yazmaya karar veriyoruz.

- login, logout, password_change, password_reset bize hazır geliyor dj_rest_auth ile ancak registration için serializer, view, url tanımlamamız gerekiyor.

- users/serializers.py create edip, register serializerımızı yazıyoruz. Bu standart bir register serializer ı dır. Tüm projelerde kullanılabilir.
  
users/serializers.py ->
```py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required = True,
        validators = [
            UniqueValidator(queryset=User.objects.all())
        ],
    )

    password = serializers.CharField(
        write_only = True,  # GET methods can not return the password
        required = True,
        validators = [
            validate_password
        ],
        style = {
            'input_type':'password',
        }
    )

    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {
            'input_type':'password',
        }
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'password2',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            data = {
                "password": "Password fields does not match!!!"
            }
            raise serializers.ValidationError(data)
        return data
```

- registration view imizle sadece create işlemi yapacağımız için Concrete viewlerden CreateAPIView den inherit ederek yazacağız.

- users/views.py ->
```py
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
```

- view imizi yazdık, şimdi onu çalıştıracak endpoint imizi url imizi yazıyoruz,

- users/urls.py ->
```py
from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
]
```

- Test ediyoruz, http://127.0.0.1:8000/users/register/  url'ine gidip, register olmaya çalışıyoruz, çalıştı ve bize girmiş olduğumuz username ve email datasını döndü.
- login ve logout çalışıyor.

- kullanıcı register olur olmaz login etmek için token create etmek için signals.py kullanıyoruz.
- users app inin içinde signals.py create edip oluşturuyoruz;

users/signals.py 
```py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

- signals.py'ı oluşturduk, ancak bundan djangonun haberi yok, signals.py ı henüz tanımıyor. signals.py ın çalışması için apps.py da, signals.py ın da altında olduğu users app imizin içinde, ready() methodunda users.signals dosyamızın da projemiz çalışırken import edilmesini belirtiyoruz.

users/apps.py 
```py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self):
        import users.signals
```

- Artık kullanıcı register olur olmaz signals ile o kullanıcı için bir de token oluşuyor.
- Test ediyoruz; Çalıştı.

- register işlemi sonrasında kullanıcı için oluşturulan token ı alıp kullanıcıya göndermemiz gerekiyor ki kullanıcı register olur olmaz geri dönen data içerisinde onun için oluşturulmuş token ı da alsın ve login olmuş olsun ve bir sonraki isteğini token ı ile göndersin. 

- Bu işlemi, yani kullanıcı register olur olmaz signal tarafından üretilen token ı, yine kullanıcıya register verisi olarak döndüğümüz datanın içerisine koymak için RegisterView imizin create() methodunu override ediyoruz;

users/views.py
```py
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['token'] = 'No token created for this user!!!'

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
```

- Yazdığımız conditionda eğer Token tablosunda bu kullanıcıya ait token varsa dönen dataya ekle, yoksa token üretilmemiş hatası dön (Belki bazı kullanıcılar için token üretilmeyecek).

- Test ediyoruz çalıştı. Artık kullanıcı register olunca, signal ile oluşturulan token datası da dönüş yaptığımız register datası içerisinde mevcut.

- dj_rest_auth paketinin sunmuş olduğu TokenSerializer ın source koduna gidip baktığımızda, başarılı bir login işleminden sonra bize sadece token key datasını gönderdiğini görüyoruz. Ancak biz bu dönen data içerisine farklı veriler de eklemek istersek (username, email, id) eğer TokenSerializer dan inherit ederek kendi CustomTokenSerializer ımızı yazarak, dönüş datasının içerisine token key ile birlikte login olan user ın başka verilerini de koyabiliriz.
- Tabi önce login olan user ın başka datalarını da koyacağımız için, önce bir UserSerializer yazacağız ki CustomTokenSerializer da hangi dataları token ile ekleyeceksek onları oluşturalım ve CustomTokenSerializer da belirtelim. 
- CustomTokenSerializer ın class Meta sını da TokenSerializer ın class Meta sını inherit ederek oluşturuyoruz ki tekrardan model = TokenModel yazmak zorunda kalmayalım. fieldlarını ise istediğimiz gibi ayarlıyoruz. user verileri de hemen yukarıda tanımladığımız UserSerializer dan gelecek olan veriler (read_only olarak)olacak.

users/serializers.py ->
```py
from dj_rest_auth.serializers import TokenSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email'
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user',
        )  
```

- Biz CustomTokenSerializer yazdık ancak, hala dj_rest_auth paketinin default olarak sunduğu TokenSerializer ı çalışmakta.

https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#

- settings.py da default olanı değil de bizim yazdığımızı kullan demek için aşağıdaki kodu settings.py' a ekliyoruz. Artık 

settings.py ->
```py
# DJ-REST-AUTH SETTINGS:
REST_AUTH = {
    # 'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer', # example
    'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer',
}
```

- Artık bizim TokenSerializer, bizim yazdığımız CustomTokenSerializer olacak.

- Test ediyoruz çalıştı, login işleminden sonra token key ile birlikte user bilgileri de (id, username, email) de dönüyor.

##### Buraya kadar standart bir authentication app
----------------------------------------------------

#### Profile Retrieve-Update

- Profile modelimiz için, profile ın sahibi olan userın sadece update yapabilmesini istiyoruz. Önce bir serializer hazırlayacağız, 
- Bu serializerda da user field ı integer olarak id si ile değil de string related field ile str daki görünümü ile görünsün istiyoruz.

- profile update için;
users/serializers.py ->
```py
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = (
            'id',
            'image',
            'about',
            'user',
        )

```

- ProfileSerializer ı kullanacak view imizi yazalım, bu viewimiz sadece profile ın sahibi user tarafından update edebilmesini sağlayacak. Bunun için Concrete View lerden RetrieveUpdateView den inherit ederek  ProfileRetrieveUpdateView imizi oluşturuyoruz. 
- RetrieveUpdateView in UpdateView den farkı -> RetrieveUpdateView: Önce detayları getirir, update eder.

users/views.py ->

```py
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Profile
from .serializers import ProfileSerializer

class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
```

- ProfileRetrieveUpdateView imizi çalıştıracak endpointimiz/urls yazıyoruz,

urls.py ->
```py
from django.urls import path, include
from .views import (
    RegisterView,
    ProfileRetrieveUpdateView,
)

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('profile/<int:pk>/', ProfileRetrieveUpdateView.as_view()),
]
```

- Test ettiğimizde, hiçbir Profile tablosunda hiçbir obje/instance create edilmediği için sonuç vermiyor.
   http://127.0.0.1:8000/users/profile/1

- Admin panelden Profile tablosunda bir instace create edip tekrar test edelim;  Evet bu sefer çalıştı.

- settings.py da MEDIA_ROOT için belirlediğimiz foldera belirlediğimiz default picture kaydedelim.

- Profile tablosunun otomatik olarak oluşturulması;
- Her user register/create edildiğinde, otomatik olarak bu user için bir de profile oluşsun istiyoruz;
- Bunun için yine token create ederken kullandığımız signals kullanacağız.

signals.py ->
```py
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

- Test ediyoruz, postmanden yeni bir user register ediyoruz, 
- http://127.0.0.1:8000/users/register/    endpointine POST methodu ile aşağıdaki datalarla istek attığımızda; 
```json
{
    "username": "user5",
    "email": "user5@gmail.com",
    "password": "use123456",
    "password2": "use123456"
}
```
- Bize aşağıdaki veriyi dönüyor ve profile tablosunda bu user'a ait bir profile create ediliyor.
```json
{
    "username": "user5",
    "email": "user5@gmail.com",
    "token": "80ffb9abbd998f3bd4b30c7640c5700b8af84fb3"
}
```


#### profile sayfasına sadece sahibi user veya admin CRUD yapabilme:
- Profile sayfasına sadece sahibi user veya adminler tarafindan CRUD yapabilme permission ı ekleme ->
users/permissions.py ->
```py
from rest_framework.permissions import BasePermission

class IsOwnerOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(request.user.is_staff or request.user == obj.user)
```


users/views.py ->
```py
from .permissions import IsOwnerOrStaff
from rest_framework.permissions import IsAuthenticated

class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrStaff, IsAuthenticated)
```
