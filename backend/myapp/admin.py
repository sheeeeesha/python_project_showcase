from django.contrib import admin
from .models import * 

admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(UserInterest)
# Register models here.