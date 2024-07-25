from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentProfileViewSet, EnrollmentViewSet, QuizResultViewSet

router = DefaultRouter()
router.register(r'profiles', StudentProfileViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'quiz-results', QuizResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]