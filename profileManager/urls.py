from django.contrib import admin
from django.urls import path

from . import views

app_name = 'profileManager'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('<int:user_id>/', views.agencyinfo, name='agencyinfo'),
]
