from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TeacherProfile
from .serializers import TeacherProfileSerializer
from api.models import Course, CustomUser, Quiz, Note
from students.models import Enrollment, QuizResult
from users.serializers import CustomUserSerializer
from students.serializers import QuizResultSerializer
class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def create_course(self, request, pk=None):
        teacher_profile = self.get_object()
        course_data = request.data
        course = Course.objects.create(**course_data, teacher=request.user)
        return Response({'status': 'course created', 'course_id': course.id}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def edit_course(self, request, pk=None):
        teacher_profile = self.get_object()
        course_id = request.data.get('course_id')
        course_data = request.data
        try:
            course = Course.objects.get(id=course_id, teacher=request.user)
            for key, value in course_data.items():
                setattr(course, key, value)
            course.save()
            return Response({'status': 'course updated'}, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def delete_course(self, request, pk=None):
        teacher_profile = self.get_object()
        course_id = request.data.get('course_id')
        try:
            course = Course.objects.get(id=course_id, teacher=request.user)
            course.delete()
            return Response({'status': 'course deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def view_students(self, request, pk=None):
        teacher_profile = self.get_object()
        course_id = request.query_params.get('course_id')
        try:
            course = Course.objects.get(id=course_id, teacher=request.user)
            students = course.enrollments.all().values_list('student', flat=True)
            student_profiles = CustomUser.objects.filter(id__in=students)
            serializer = CustomUserSerializer(student_profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def view_student_performance(self, request, pk=None):
        teacher_profile = self.get_object()
        course_id = request.query_params.get('course_id')
        student_id = request.query_params.get('student_id')
        try:
            course = Course.objects.get(id=course_id, teacher=request.user)
            enrollments = Enrollment.objects.filter(course=course, student_id=student_id)
            if not enrollments.exists():
                return Response({'error': 'Student not enrolled in this course'}, status=status.HTTP_404_NOT_FOUND)
            quiz_results = QuizResult.objects.filter(student_id=student_id, quiz__course=course)
            serializer = QuizResultSerializer(quiz_results, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)