from atexit import register
from django.contrib import admin

# Register your models
from .models import *

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','gender','locality','city','pin','state','mobile','job_city','profile_image','my_file','experience','education','projects','skills','awards','languages']
