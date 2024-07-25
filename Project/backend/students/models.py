from django.db import models
from django.conf import settings
from api.models import Course, Quiz

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    enrolled_courses = models.ManyToManyField(Course, through='students.Enrollment', related_name='enrolled_students')
    performance_analytics = models.JSONField(default=dict)

class Enrollment(models.Model):
    student_profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_enrollments')
    date_enrolled = models.DateTimeField(auto_now_add=True)

class QuizResult(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_results')
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)