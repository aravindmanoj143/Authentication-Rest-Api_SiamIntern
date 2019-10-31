from rest_framework.permissions import IsAuthenticated
from .serializers import ClientSerializer, LoginSerializer
from .models import Client
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics


class Client_view(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "username": user.username}, status=200,)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response(status=204)
