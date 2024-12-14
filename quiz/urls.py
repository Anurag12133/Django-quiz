from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.get_question, name='get_question'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('results/', views.quiz_results, name='quiz_results'),
]
