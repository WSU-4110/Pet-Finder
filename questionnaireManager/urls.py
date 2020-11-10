from django.contrib import admin
from django.urls import path

from . import views

app_name='questionnaireManager'
urlpatterns = [
	path('', views.quiz, name='quiz'),
]
