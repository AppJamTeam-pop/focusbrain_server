from django.db.transaction import atomic
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import CsrfExemptSessionAuthentication
from focus.models import Focus
from focus.serializers import FocusSerializer


class FocusView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    @atomic
    def post(self, request: Request) -> Response:
        serializer = FocusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)


class FocusRankView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        focus = Focus.objects.all()\
            .order_by('-in_time')\
            .select_related('user')
        serializer = FocusSerializer(focus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyFocusRankView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        date = request.GET.get('date')
        all_focus = Focus.objects.filter(date=date)\
            .order_by('-date')\
            .select_related('user')

        user_focus = Focus.objects.filter(
            date=date,
            user=request.user
        )\
            .order_by('-date')\
            .select_related('user')\
            .first()

        index = list(all_focus).index(user_focus) + 1

        data = {
            'rank': index,
            'in_time': user_focus.in_time
        }

        return Response(data, status=status.HTTP_200_OK)
