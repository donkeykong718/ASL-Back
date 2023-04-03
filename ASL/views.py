from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, permissions, status
from .models import ChatBox, Messages
from .serializers import ChatBoxSerializer, MessagesSerializer, UserSerializer
# Create your views here.


class ChatBoxViewSet(viewsets.ModelViewSet):
    queryset = ChatBox.objects.all()
    serializer_class = ChatBoxSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(creator=self.request.user)
      
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password', None)
        serializer.save(password=make_password(password))
    def perform_update(self, serializer):
        password = serializer.validated_data.get('password', None)
        serializer.save(password=make_password(password))