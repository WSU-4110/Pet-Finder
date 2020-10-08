from django.contrib import admin
from django.urls import path

from . import views

app_name='startpage'
urlpatterns = [
	path('', views.home, name='home'),
]
