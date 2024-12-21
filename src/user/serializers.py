from rest_framework import serializers

from user.exception import UserException
from user.models import User


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if user:
            raise UserException.UserAlreadyExistsException
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)