# from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

from django.db import models

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
    thumbnail = models.ImageField(upload_to='backend\myproject\media\project_thumbnail', null=True, blank=True)

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

