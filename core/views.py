from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Profile, Skill, UserEducation, UserJob, UserProject, UserSkill
from .serializers import CreateUserSkillSerializer, GetUserSkillSerializer, ProfileSerializer, SkillSerializer, UserEducationSerializer, UserJobSerializer, UserProjectSerializer


class ProfileAPIView(RetrieveUpdateAPIView):
    
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUser, ]


class UserSkillViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetUserSkillSerializer

        return CreateUserSkillSerializer

    def get_queryset(self):
        return UserSkill.objects.filter(user=self.request.user).all()


class UserEducationViewSet(ModelViewSet):

    serializer_class = UserEducationSerializer    
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return UserEducation.objects.filter(user=self.request.user).all()


class UserJobViewSet(ModelViewSet):

    serializer_class = UserJobSerializer    
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return UserJob.objects.filter(user=self.request.user).all()


class UserProjectViewSet(ModelViewSet):

    serializer_class = UserProjectSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return UserProject.objects.filter(user=self.request.user).all()