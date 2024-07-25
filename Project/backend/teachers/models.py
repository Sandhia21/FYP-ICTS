from django.db import models
from django.conf import settings
from api.models import Course

class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    courses = models.ManyToManyField(Course, related_name='teachers')
