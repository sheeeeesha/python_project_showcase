# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



def get_current_user():
    return get_user_model().objects.get(pk=1)  # Replace with appropriate logic to get the current authenticated user



class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=200)
    start_date = models.DateField()
    num_people_required = models.IntegerField()
    pid = models.CharField(primary_key=True, max_length=20)
    tags = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user)

    def __str__(self):
        return self.project_name

    def add_join_request(self, user):
        join_request = JoinRequest.objects.create(user=user, project=self)
        return join_request
    
    @classmethod
    def get_projects_created_by_user(cls, user):
        return cls.objects.filter(created_by=user)


class JoinRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Join request from {self.user.username} for project {self.project.project_name}"

    @classmethod
    def accept(cls, join_request):
        # Create a UserProject entry for the accepted join request
        UserProject.objects.create(user=join_request.user, project=join_request.project)
        # Delete the join request
        join_request.delete()

    @classmethod
    def reject(cls, join_request):
        # Delete the join request
        join_request.delete()

    @staticmethod
    def get_requests_for_projects_created_by_user(user):
        return JoinRequest.objects.filter(project__created_by=user)
    

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} is working on {self.project.project_name}"

    
class Paper(models.Model):
    paper_name = models.CharField(max_length=100)
    start_date = models.DateField()
    num_people_required = models.IntegerField()
    tags = models.CharField(max_length=100)
    paperid = models.CharField(primary_key=True, max_length=20)




class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)


    '''
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    prn = models.CharField(primary_key=True, max_length=20)
    availability = models.BooleanField(default=True)
'''

