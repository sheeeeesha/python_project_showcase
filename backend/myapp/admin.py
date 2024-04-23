from django.contrib import admin
from .models import * 

admin.site.register(Project)
admin.site.register(UserProject)
admin.site.register(UserInterest)
admin.site.register(JoinRequest)
# Register models here.