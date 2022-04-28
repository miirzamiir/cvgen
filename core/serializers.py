from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Profile, Skill, UserEducation, UserJob, UserProject, UserSkill

class ProfileSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        print(validated_data)
        return super().create(validated_data)

    class Meta:
        model = Profile
        fields = (
            'image', 'phone_number', 'location', 'birthday',
            'job_title' , 'is_employed', 'company', 'bio'
        )
        read_only_fields = ('user', )


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id', 'name')


class GetUserSkillSerializer(ModelSerializer):
    
    skill = serializers.StringRelatedField()
    
    class Meta:
        model = UserSkill
        fields = ('skill', 'level')


class CreateUserSkillSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)


    class Meta:
        model = UserSkill
        fields = ('skill', 'level')


class UserEducationSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)

    class Meta:
        model = UserEducation
        fields = (
            'id', 'degree', 'field', 'educational_center',
            'start_year', 'finish_year', 'still_going', 'description'
        )


class UserJobSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)

    class Meta:
        model = UserJob
        fields = (
            'id', 'company', 'position',
            'start_year', 'finish_year', 'still_going', 'description'
        )


class UserProjectSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)


    class Meta:
        model = UserProject
        fields = (
            'id', 'name', 'url', 'description'
        )