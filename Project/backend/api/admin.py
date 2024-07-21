from django.contrib import admin
from .models import CustomUser, Course, Enrollment

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Enrollment)