from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProfileAPIView, SkillViewSet, UserEducationViewSet, UserJobViewSet, UserProjectViewSet, UserSkillViewSet

router = DefaultRouter()
router.register('skills', SkillViewSet, basename='skill-viewset')
router.register('my_skills', UserSkillViewSet, basename='userskill-viewset')
router.register('education', UserEducationViewSet, basename='usereducation-viewset')
router.register('jobs', UserJobViewSet, basename='userjob-viewset')
router.register('projects', UserProjectViewSet, basename='userproject-viewset')


urlpatterns = [
    path('profile/', ProfileAPIView.as_view()),
] + router.urls