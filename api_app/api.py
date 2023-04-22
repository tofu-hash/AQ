from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth import get_user_model  # If used custom user model
from api_app.base.response import CustomResponse
from django.contrib.auth import authenticate, login, logout
from api_app.models import Question
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *


class CustomCreateAPIView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return CustomResponse(serializer.data, message='Объект создан').good(_status=status.HTTP_201_CREATED,
                                                                             headers=headers)


class CreateUserView(CustomCreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            data = {'username': username}
            return CustomResponse(data, message='Выполнен вход в профиль').good()
        else:
            return CustomResponse(message='Вход в профиль не выполнен').bad(_status=status.HTTP_401_UNAUTHORIZED)


class LogoutUserView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return CustomResponse(message='Выполнен выход из профиля').good()


class CreateQuestionView(CustomCreateAPIView):
    model = Question
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CreateQuestionSerializer


class GetCurrentUserQuestions(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = GetQuestionSerializer
