from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CreateUserAPIView, ManageUserAPIView

router = DefaultRouter()

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('me/', ManageUserAPIView.as_view()),
    
]