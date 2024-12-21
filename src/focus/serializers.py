from rest_framework import serializers

from focus.models import Focus


class FocusSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = Focus
        fields = '__all__'

        extra_kwargs = {
            'user': {'required': False},
        }