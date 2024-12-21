from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import CsrfExemptSessionAuthentication
from user.models import User
from user.serializers import MyUserInfoSerializer


class MyInfoView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        myinfo = User.objects.filter(id=request.user.id).first()
        serializer = MyUserInfoSerializer(myinfo)
        return Response(serializer.data, status=status.HTTP_200_OK)
