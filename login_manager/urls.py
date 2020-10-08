from django.contrib import admin
from django.urls import path

from . import views

app_name='login_manager'
urlpatterns = [
	path('', views.login_page, name='login_page'),
	path('register/', views.register_page, name='register_page'),
	#path('login/auth/', views.login_user, name='login_user'),
	#path('user/check/', views.check_userExists, name='check_user'),
	#path('register/user/', views.register_user, name='register_user'),
	#path('forget/', views.forget_user, name='forget_user'),
	#path('forgot/', views.forgot_username, name='forgot_user'),
]
