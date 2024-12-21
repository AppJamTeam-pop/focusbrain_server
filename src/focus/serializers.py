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


class MyFocusRankSerializer(serializers.ModelSerializer):
    rank = serializers.SerializerMethodField()

    class Meta:
        model = Focus
        fields = ('in_time', 'rank')

    def get_rank(self, obj):
        request = self.context.get('request')
        date = request.GET.get('date')
        all_focus = Focus.objects.filter(date=date) \
            .order_by('-date') \
            .select_related('user')

        return list(all_focus).index(obj) + 1