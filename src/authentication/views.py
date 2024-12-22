from django.contrib.auth import authenticate, login, logout
from django.db.transaction import atomic
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import CsrfExemptSessionAuthentication
from authentication.exception import UserException
from authentication.serializers import UserSignupSerializer, SigninSerializer


class SigninView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]

    @atomic
    def post(self, request: Request) -> Response:
        serializer = SigninSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not (user := authenticate(request, **serializer.validated_data)):
            raise UserException.UserNotFoundException
        login(request, user)
        return Response(status=status.HTTP_200_OK)


class SignupView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]

    @atomic
    def post(self, request: Request) -> Response:
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request) -> Response:
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)