
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserNotification, LoginLog

class YourNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ('password', 'email')

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    image_name = serializers.CharField(max_length=300)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'image_name',
        )

class EmptySerializer(serializers.Serializer):
    pass