from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    LoginSerializers,
    RegisterSerializers,
    ProfileSerializer,
    FeedbackSerializers,
)
from .models import Feedback


# Регистрация
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]


# Авторизация
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Login failed'}, status=status.HTTP_400_BAD_REQUEST)


# Выход из аккаунта
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


# Профиль пользователя
class ProfileView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


# Отправка обратной связи
class FeedbackSendView(generics.CreateAPIView):
    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        feedback = serializer.save()
        subject = f'Обратная связь от {feedback.name}'
        full_message = (
            f'Имя: {feedback.name}\n'
            f'Email: {feedback.email}\n'
            f'Message: {feedback.message}'
        )

        send_mail(
            subject,
            full_message,
            feedback.email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
