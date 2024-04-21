from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from .forms import ProjectForm
from .models import Project

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'main.html') # Redirect to home page after successful login
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can log the user in immediately after registration
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # Include request.FILES for file upload
        if form.is_valid():
            form.save()  # Save the project object along with the uploaded thumbnail image
            return redirect('available_projects')  
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})



def join_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'endpoint.html')  # Redirect to the home page after successful project creation
    else:
        form = ProjectForm()
    return render(request, 'join_project.html', {'form': form})

def available_projects(request):
    projects = Project.objects.all()
    for project in projects:
        project.has_thumbnail = bool(project.thumbnail)  # Check if project has a thumbnail
    return render(request, 'available_projects.html', {'projects': projects})

def profile(request):
    return render(request, 'index.html')
def home(request):
    return render(request,'main.html')

