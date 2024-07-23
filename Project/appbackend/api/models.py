from django.db import models
from users.models import CustomUser

from django.db import models
from users.models import CustomUser

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='course_pics/', blank=True, null=True)
    teacher = models.ForeignKey(CustomUser, related_name='courses', on_delete=models.CASCADE)
    lecture_hours = models.IntegerField()
    credits = models.IntegerField()
    students = models.ManyToManyField(CustomUser, related_name='enrolled_courses', blank=True)

class TableOfContent(models.Model):
    course = models.ForeignKey(Course, related_name='table_of_contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Note(models.Model):
    table_of_content = models.ForeignKey(TableOfContent, related_name='notes', on_delete=models.CASCADE)
    content = models.TextField()

class Quiz(models.Model):
    table_of_content = models.ForeignKey(TableOfContent, related_name='quizzes', on_delete=models.CASCADE)
    questions = models.TextField()  # This can be further structured if needed

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
