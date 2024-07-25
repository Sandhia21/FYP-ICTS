from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, TableOfContentViewSet, NoteViewSet, QuizViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'table_of_contents', TableOfContentViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
