from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfile, Enrollment, QuizResult
from .serializers import StudentProfileSerializer, EnrollmentSerializer, QuizResultSerializer
from api.models import Course

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def join_course(self, request, pk=None):
        student_profile = self.get_object()
        course_code = request.data.get('course_code')
        course_key = request.data.get('course_key')
        try:
            course = Course.objects.get(code=course_code, course_key=course_key)
            Enrollment.objects.create(student=request.user, course=course)
            return Response({'status': 'course joined'}, status=status.HTTP_201_CREATED)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found or invalid course key'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def exit_course(self, request, pk=None):
        student_profile = self.get_object()
        course_id = request.data.get('course_id')
        try:
            enrollment = Enrollment.objects.get(student=request.user, course_id=course_id)
            enrollment.delete()
            return Response({'status': 'course exited'}, status=status.HTTP_204_NO_CONTENT)
        except Enrollment.DoesNotExist:
            return Response({'error': 'Enrollment not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def quiz_results(self, request, pk=None):
        student_profile = self.get_object()
        quiz_results = QuizResult.objects.filter(student=request.user)
        serializer = QuizResultSerializer(quiz_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class QuizResultViewSet(viewsets.ModelViewSet):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer