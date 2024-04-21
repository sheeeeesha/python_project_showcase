from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name','project_desc','num_people_required','start_date','pid','tags','thumbnail']
