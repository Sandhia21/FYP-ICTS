from django.db import models
from users.models import CustomUser

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='course_pics/', blank=True, null=True)
    teacher = models.ForeignKey(CustomUser, related_name='courses', on_delete=models.CASCADE)

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)