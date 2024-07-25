from rest_framework import serializers
from .models import StudentProfile, Enrollment, QuizResult

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['user', 'enrolled_courses', 'performance_analytics']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'date_enrolled']

class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ['student', 'quiz', 'score', 'date_taken']