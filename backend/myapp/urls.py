from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_project/', views.create_project, name='create_project'),
    path('available_projects/', views.available_projects, name='available_projects'),
    path('profile/',views.index,name='profile'),
    path('home/', views.home, name='home'),
    # Add more URL patterns as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)