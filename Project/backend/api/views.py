from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from .models import Course, TableOfContent, Note, Quiz, Enrollment
from .serializers import CourseSerializer, TableOfContentSerializer, NoteSerializer, QuizSerializer, EnrollmentSerializer
from users.models import CustomUser
from ai_trainer import AITrainer

# Configure API key
AITrainer.configure_api_key("YOUR_OPENAI_API_KEY_HERE")

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

    @action(detail=False, methods=['post'], url_path='self-enroll')
    def self_enroll(self, request):
        course_code = request.data.get('course_code')
        course_key = request.data.get('course_key')

        try:
            course = Course.objects.get(code=course_code, course_key=course_key)
            student = request.user
            if not student.is_authenticated:
                return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

            enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)
            if created:
                return Response({'status': 'student enrolled'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'student already enrolled'}, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found or invalid course key'}, status=status.HTTP_404_NOT_FOUND)

class TableOfContentViewSet(viewsets.ModelViewSet):
    queryset = TableOfContent.objects.all()
    serializer_class = TableOfContentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        table_of_content = serializer.save()

        # Generate notes and quiz using AITrainer
        notes_content = AITrainer.generate_notes(table_of_content.title)
        quiz_content = AITrainer.generate_quiz(table_of_content.title)

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
