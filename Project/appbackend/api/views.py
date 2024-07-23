
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Course, TableOfContent, Note, Quiz,Enrollment
from .serializers import CourseSerializer, TableOfContentSerializer, NoteSerializer, QuizSerializer,EnrollmentSerializer
from .ai_trainer import AITrainer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class TableOfContentViewSet(viewsets.ModelViewSet):
    queryset = TableOfContent.objects.all()
    serializer_class = TableOfContentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        table_of_content = serializer.save()
        
        # Generate notes and quiz using AITrainer
        ai_trainer = AITrainer(api_key="YOUR_OPENAI_API_KEY")
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