from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_project/', views.create_project, name='create_project'),
    #path('join_project/', views.join_project, name='join_project'),
    path('available_projects/', views.available_projects, name='available_projects'),
    path('profile/', views.index, name='profile'),
    path('home/', views.home, name='home'),

    # Add more URL patterns as needed
]
