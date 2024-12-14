# Quiz

This is a simple Quiz Application built with Django. The app allows users to answer randomly selected multiple-choice questions and view their results (correct/incorrect answers) at the end.

-> Due to time constraint i made a simple ui using HTML in templates.




## Setup and Installation

```python
git clone https://github.com/Anurag12133/Django-quiz
cd Django-quiz


```

## Set Up a Virtual Environment 

```
python -m venv env
source env/bin/activate  #linux/macos 
env\Scripts\activate      #windows
```
## Install django
```
pip install django
```

## Run Database Migrations
```
python manage.py makemigrations
python manage.py migrate
```

## Load Questions into the Database
```
python manage.py load_questions
```

## Run the Development Server
```
python manage.py runserver
```

