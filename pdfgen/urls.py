
from django.urls import path
from .views import cvgen, test

urlpatterns = [
    path('resume/', cvgen.as_view()),
    path('pdf/', test.as_view()),
]