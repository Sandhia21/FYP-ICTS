from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Course, TableOfContent, Note, Quiz, Enrollment
from .serializers import CourseSerializer, TableOfContentSerializer, NoteSerializer, QuizSerializer, EnrollmentSerializer
from ai_trainer import AITrainer  # Import AITrainer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def enroll_student(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')
        try:
            student = CustomUser.objects.get(id=student_id)
            Enrollment.objects.create(student=student, course=course)
            return Response({'status': 'student enrolled'}, status=status.HTTP_201_CREATED)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def self_enroll(self, request):
        course_code = request.data.get('course_code')
        course_key = request.data.get('course_key')
        try:
            course = Course.objects.get(code=course_code, course_key=course_key)
            Enrollment.objects.create(student=request.user, course=course)
            return Response({'status': 'self enrolled'}, status=status.HTTP_201_CREATED)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found or invalid course key'}, status=status.HTTP_404_NOT_FOUND)

class TableOfContentViewSet(viewsets.ModelViewSet):
    queryset = TableOfContent.objects.all()
    serializer_class = TableOfContentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        table_of_content = serializer.save()
        
        # Generate notes and quiz using AITrainer
        ai_trainer = AITrainer
        notes_content = ai_trainer.generate_notes(table_of_content.title)
        quiz_content = ai_trainer.generate_quiz(table_of_content.title)
        
        # Save the generated notes and quiz
        Note.objects.create(table_of_content=table_of_content, content=notes_content)
        Quiz.objects.create(table_of_content=table_of_content, questions=quiz_content)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]