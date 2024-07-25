from django.db import models
from users.models import CustomUser
import uuid
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='course_pics/', blank=True, null=True)
    teacher = models.ForeignKey(CustomUser, related_name='courses', on_delete=models.CASCADE)
    lecture_hours = models.IntegerField(default=0)
    credits = models.IntegerField(default=0)
    students = models.ManyToManyField(CustomUser, through='Enrollment', related_name='enrolled_courses', blank=True)
    course_key = models.CharField(max_length=20, unique=True, default=uuid.uuid4)





class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='api_enrollments')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='api_enrollments')
    date_enrolled = models.DateTimeField(auto_now_add=True)

class TableOfContent(models.Model):
    course = models.ForeignKey(Course, related_name='table_of_contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Note(models.Model):
    table_of_content = models.ForeignKey(TableOfContent, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()

class Quiz(models.Model):
    table_of_content = models.ForeignKey(TableOfContent, related_name='quizzes', on_delete=models.CASCADE)
    questions = models.TextField()  # This can be further structured if needed    