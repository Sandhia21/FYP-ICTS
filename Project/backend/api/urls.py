from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CourseViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]