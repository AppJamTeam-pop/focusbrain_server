from rest_framework import serializers

from focus.serializers import FocusSerializer
from user.models import User


class MyUserInfoSerializer(serializers.ModelSerializer):
    focus = FocusSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'focus')
