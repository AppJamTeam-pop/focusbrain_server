from rest_framework import serializers

from focus.models import Focus


class FocusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateField('%Y-%m-%d')
    in_time = serializers.FloatField()
    out_count = serializers.IntegerField()
    username = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        return Focus.objects.create(**validated_data)

    def get_username(self, data):
        return data.user.username
