from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserCreationForm
from .forms import ProjectForm

from .models import Project
from .models import JoinRequest

from django.contrib.auth.decorators import login_required
from django.db import models


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



@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # Include request.FILES for file upload
        if form.is_valid():
            form.save()  # Save the project object along with the uploaded thumbnail image
            return redirect('home')  
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})



@login_required
def join_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'endpoint.html')  # Redirect to the home page after successful project creation
    else:
        form = ProjectForm()
    return render(request, 'join_project.html', {'form': form})




@login_required
def available_projects(request):
    projects = Project.objects.all()
    for project in projects:
        project.has_thumbnail = bool(project.thumbnail)  # Check if project has a thumbnail
    return render(request, 'available_projects.html', {'projects': projects})




@login_required
def user_projects(request): #created by current user
    user = request.user
    user_projects = Project.get_projects_created_by_user(user)
    for project in user_projects:
        project.has_thumbnail = bool(project.thumbnail)  # Check if project has a thumbnail
    return render(request, 'created_projects.html', {'projects': user_projects})


# managing and showing requests


@login_required
def send_join_request(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=project_id)
        
        # Check if the user has already sent a join request
        if project.joinrequest_set.filter(user=request.user).exists():
            return render(request, 'error.html', {'error_message': 'You have already sent a join request for this project.'})
        
        # Add the join request
        project.add_join_request(request.user)
        
        return redirect('available_projects')

    return redirect('available_projects')



@login_required
def user_join_requests(request):
    current_user = request.user
    join_requests = JoinRequest.get_requests_for_projects_created_by_user(current_user)
    return render(request, 'join_requests.html', {'join_requests': join_requests})



@login_required
def accept_join_request(request, join_request_id):
    join_request = get_object_or_404(JoinRequest, pk=join_request_id)
    if request.method == 'POST':
        # Accept the join request
        join_request.accept(join_request)
        return redirect('user_join_requests')  # Redirect to the user_join_requests page after accepting the request
    return render(request, 'join_requests.html', {'join_request': join_request})



@login_required
def reject_join_request(request, join_request_id):
    join_request = get_object_or_404(JoinRequest, pk=join_request_id)
    if request.method == 'POST':
        # Reject the join request
        join_request.reject(join_request)
        return redirect('user_join_requests')  # Redirect to the user_join_requests page after rejecting the request
    return render(request, 'join_requests.html', {'join_request': join_request})



@login_required
def profile(request): 

        user = request.user
       # if user.is_authenticated:
       #     projects = ProjectUser.objects.filter(user=request.user)
       # else:
        #    projects = None 
        
        context = {
            'user' : user,
           # 'projects': projects,
        }
        return render(request, 'index.html', context)



@login_required
def home(request):
    return render(request,'main.html')

    

