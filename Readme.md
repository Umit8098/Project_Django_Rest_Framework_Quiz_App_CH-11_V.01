<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Quiz_App</h1>


<div align="center">
  <h3>
    <a href="http://umit8102.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="http://umit8102.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

![screenshot](project_screenshot/quiz_app.gif)

---
- Quiz App Test On Postman
![screenshot](project_screenshot/quiz_app_quiz.gif)

---
- User/Authentication App Test On Postman
![screenshot](project_screenshot/quiz_app_user.gif)

---
- Quiz App Project Schema
![screenshot](project_screenshot/quiz_app_shema.jpg)


## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Djago Rest Framework


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

## About This Project
- Quiz Application API service.
- Using the django-nested-admin package in the admin panel.

<hr>

- Quiz Application API service.
- admin panelde django-nested-admin paketi kullanımı.

## Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [django-nested-admin](https://django-nested-admin.readthedocs.io/en/latest/)
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
