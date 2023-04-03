from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, permissions, status
from .models import ChatBox, Messages
from .serializers import ChatBoxSerializer, MessagesSerializer, UserSerializer
# Create your views here.
