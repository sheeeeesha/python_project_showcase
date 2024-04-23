# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import User

'''
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    prn = models.CharField(primary_key=True, max_length=20)
    availability = models.BooleanField(default=True)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=200)
    start_date = models.DateField()
    num_people_required = models.IntegerField()
    pid = models.CharField(primary_key=True, max_length=20)
    tags = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    joinRequests = models.ManyToManyField(User, related_name='join_requests', blank=True)
'''

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=200)
    start_date = models.DateField()
    num_people_required = models.IntegerField()
    pid = models.CharField(primary_key=True, max_length=20)
    tags = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    created_by = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)  # Link project to its creator
    joinRequests = models.ManyToManyField(User, related_name='join_requests', blank=True)

    def add_join_request(self, user):
        """Add a join request for the given user."""
        if user != self.created_by:  # Only allow join requests from users other than the creator
            self.joinRequests.add(user)

    def remove_join_request(self, user):
        """Remove a join request for the given user."""
        self.joinRequests.remove(user)

    def approve_join_request(self, user):
        """Approve a join request for the given user."""
        if user in self.joinRequests.all():
            # Logic to approve the user's request (e.g., add them to the project team)
            # Here you can implement your specific business logic
            pass

    def deny_join_request(self, user):
        """Deny a join request for the given user."""
        self.joinRequests.remove(user)

    def is_creator(self, user):
        """Check if the given user is the creator of the project."""
        return user == self.created_by

    
class Paper(models.Model):
    paper_name = models.CharField(max_length=100)
    start_date = models.DateField()
    num_people_required = models.IntegerField()
    tags = models.CharField(max_length=100)
    paperid = models.CharField(primary_key=True, max_length=20)

class ProjectUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.CharField(max_length=100)

