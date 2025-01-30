<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Quiz_App</h1>

<p align="center"><strong>🎓 A Quiz API application that allows users to create quizzes, manage questions, and organize their learning process 🎓</strong></p>

<!-- <p align="center">🎓 Kullanıcıların quiz oluşturmasına, soruları yönetmesine ve öğrenme süreçlerini organize etmesine olanak tanıyan bir Quiz API uygulaması 🎓</p> -->

<!-- <div align="center">
  <h3>
    <a href="http://umit8102.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="http://umit8102.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div> -->

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [API Endpoints](#api-endpoints)
  - [User/Authentication Endpoints:](#userauthentication-endpoints)
  - [Quiz Endpoints:](#quiz-endpoints)
- [API Testing](#api-testing)
- [Overview](#overview)
  - [User Authentication Test](#user-authentication-test)
  - [Web browsable API Test](#web-browsable-api-test)
  - [Quiz App Test](#quiz-app-test)
  - [Quiz App Project Schema](#quiz-app-project-schema)
- [Built With](#built-with)
- [How To Use](#how-to-use)
  - [Example Usage](#example-usage)
- [Key Features](#key-features)
- [Contact](#contact)

<!-- OVERVIEW -->

## API Endpoints

This API provides the following endpoints:

### User/Authentication Endpoints:

| Method | URL                                                          | Explanation           |
|--------|--------------------------------------------------------------|-----------------------|
| POST   | `https://umit8102.pythonanywhere.com/users/register/`        | New user registration |
| POST   | `https://umit8102.pythonanywhere.com/users/auth/login/`      | User login            |
| POST   | `https://umit8102.pythonanywhere.com/users/auth/logout/`     | User logout           |


### Quiz Endpoints:

| Method | URL                                                                   | Explanation                          |
|--------|-----------------------------------------------------------------------|--------------------------------------|
| GET    | `https://umit8102.pythonanywhere.com/quiz/`                           | List all Quiz Categories             |
| GET    | `https://umit8102.pythonanywhere.com/quiz/quiz`                       | List quizzes of all Categories       |
| GET    | `https://umit8102.pythonanywhere.com/quiz/question/`                  | List questions of all quizzes        |
| GET    | `https://umit8102.pythonanywhere.com/quiz/quiz/?search=angu`          | quiz search                          |
| GET    | `https://umit8102.pythonanywhere.com/quiz/question/?quiz__title=React`| quiz filter                          |


## API Testing

Postman Collection contains the necessary requests to test each endpoint of your API. You can use it to quickly understand the functionality of the API.

To test APIs via Postman, you can follow the steps below:

1. Install Postman (if not installed): [Postman İndir](https://www.postman.com/downloads/).
2. This [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-e7678a3c-288b-4c80-b639-b1a1b6b42051?action=share&creator=17531143) download and import.
3. Start testing APIs via Postman.


**Postman Collection Link:**  
[Quiz App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-e7678a3c-288b-4c80-b639-b1a1b6b42051?action=share&creator=17531143)


## Overview

The Quiz API application allows users to create quizzes in various categories, add questions and manage these contents. Features of the application:
- User authentication and authorization.
- CRUD operations for quiz and question management.
- Search and filtering features.
- Easy content management with nested structure in Django admin panel.

---

Quiz API uygulaması, kullanıcıların çeşitli kategorilerde quiz oluşturmasına, sorular eklemesine ve bu içerikleri yönetmesine olanak tanır. Uygulamanın özellikleri:
- Kullanıcı doğrulama ve yetkilendirme.
- Quiz ve soru yönetimi için CRUD işlemleri.
- Arama ve filtreleme özellikleri.
- Django admin panelinde nested yapı ile kolay içerik yönetimi.

### User Authentication Test
<!-- ![screenshot](project_screenshot/quiz_app_user.gif) -->
<img src="project_screenshot/quiz_app_user.gif" alt="User/Authentication Test" width="400"/>

➡ Testing user authentication processes with Postman.

---
### Web browsable API Test
<!-- ![screenshot](project_screenshot/quiz_app.gif) -->
<img src="project_screenshot/quiz_app.gif" alt="Web browsable API" width="400"/>

➡ The process of testing the API in the web interface provided by Django Rest Framework.

---

### Quiz App Test
<!-- ![screenshot](project_screenshot/quiz_app_quiz.gif) -->
<img src="project_screenshot/quiz_app_quiz.gif" alt="Quiz App Test" width="400"/>

➡ Testing the Quiz App API with Postman.

---

### Quiz App Project Schema
<!-- ![screenshot](project_screenshot/quiz_app_shema.jpg) -->
<img src="project_screenshot/quiz_app_shema.jpg" alt="Quiz App Project Schema" width="400"/>

➡ Schema that represents the application's data model relationships and structure.


## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->
This project is built with the following tools and libraries:

- [Django Rest Framework](https://www.django-rest-framework.org/): A powerful framework for developing REST APIs.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/): User authentication and authorization.
- [django-nested-admin](https://django-nested-admin.readthedocs.io/en/latest/): Hierarchical structure management in Django admin panel.
- [django-filter](https://django-filter.readthedocs.io/en/stable/): To facilitate data filtering operations.



## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Rest_Framework_Quiz_App_CH-11_V.01.git) 

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin. 

```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Quiz_App_CH-11_V.01.git

# Install dependencies
    $ python -m venv env
    $ python -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...
"""

# Run the app
    $ python manage.py runserver
```

### Example Usage

1. **List Quiz:**
   - URL: `https://umit8102.pythonanywhere.com/quiz/quiz`
   - Method: `GET`

2. **Filter Question Quiz:**
   - URL: `https://umit8102.pythonanywhere.com/quiz/question/?quiz__title=React`
   - Method: `GET`



## Key Features

- **Quiz Management:** Users can create and update quizzes in various categories.  
- **Question Management:** Questions can be added, edited and deleted for each quiz.  
- **User Authorization:** Registered users have quiz and question management privileges.  
- **Admin Panel:** Hierarchical data management with Django Nested Admin.  
- **Search and Filtering:** Advanced filtering options on quiz and question data.  
- **Responsive API:** Secure and high-performance API with Django Rest Framework.

---

- **Quiz Yönetimi:** Kullanıcılar çeşitli kategorilerde quizler oluşturabilir ve güncelleyebilir.  
- **Soru Yönetimi:** Her quiz için sorular eklenebilir, düzenlenebilir ve silinebilir.  
- **Kullanıcı Yetkilendirme:** Kayıtlı kullanıcılar quiz ve soru yönetim yetkilerine sahip olur.  
- **Admin Panel:** Django Nested Admin ile hiyerarşik veri yönetimi.  
- **Arama ve Filtreleme:** Quiz ve soru verileri üzerinde gelişmiş filtreleme seçenekleri.  
- **Duyarlı API:** Django Rest Framework ile güvenli ve performanslı API.  


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- **GitHub**: [@Umit8098](https://github.com/Umit8098)

- **LinkedIn**: [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
