from django.contrib import admin
from .models import *

admin.site.register([Lesson, Modules, Student, Course, Group, Teacher])
