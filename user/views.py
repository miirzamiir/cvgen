from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ManageUserSerializer, CreateUserSerializer


class CreateUserAPIView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CreateUserSerializer


class ManageUserAPIView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = ManageUserSerializer
    permission_classes = [IsAuthenticated,]
    

    def get_object(self):
        return get_user_model().objects.get(id=self.request.user.id)
    