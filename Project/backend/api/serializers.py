from rest_framework import serializers
from .models import Course, TableOfContent, Note, Quiz, Enrollment

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'table_of_content', 'content']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'table_of_content', 'questions']

class TableOfContentSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = TableOfContent
        fields = ['id', 'course', 'title', 'notes', 'quizzes']

class CourseSerializer(serializers.ModelSerializer):
    table_of_contents = TableOfContentSerializer(many=True, read_only=True)
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'description', 'picture', 'teacher', 'lecture_hours', 'credits', 'students', 'table_of_contents', 'course_key']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'date_enrolled']