from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model


class CreateUserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        write_only_fields = ('password', )
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password', },
            }
        }


class ManageUserSerializer(serializers.ModelSerializer):
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        write_only_fields = ('password', )
        read_only_fields = ('email', )
        extra_kwargs = {
            'password' : {
                'write_only':True,
                'style' : {'input_type' : 'password', },
            }
        }
