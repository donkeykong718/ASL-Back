from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.contrib.auth.models import User
from django.urls import path, include, re_path

from chats.api.views import ConversationViewSet, MessageViewSet
from chats.api.serializers import UserSerializer
from django.contrib.auth.hashers import make_password


from django.contrib.auth import get_user_model
from rest_framework import status, viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import authentication, permissions


class CustomRouter(DefaultRouter):
    routes = []


# class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_field = "username"

#     def get_queryset(self, *args, **kwargs):
#         assert isinstance(self.request.user.id, int)
#         return self.queryset.filter(id=self.request.user.id)

#     def get_serializer_context(self):
#         return {"request": self.request, "user": self.request.user}

#     @action(detail=True, methods=["POST"], permission_classes=[permissions.AllowAny], url_path="register", )
#     def create(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         user.set_password(user.password)
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({"token": token.key}, status=status.HTTP_201_CREATED)

#     @action(detail=True, methods=["POST"], permission_classes=[permissions.AllowAny], url_path="login",)
#     def login(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key}, status=status.HTTP_200_OK)

#     @action(detail=True, methods=["POST"], url_path="logout",)
#     def logout(self, request):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(detail=True, methods=["POST"], url_path="change-password",)
#     def change_password(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = request.user
#         user.set_password(serializer.validated_data["password"])
#         user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(detail=True, methods=["POST"], url_path="reset-password",)
#     def reset_password(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = User.objects.get(email=serializer.validated_data["email"])
#         user.set_password(serializer.validated_data["password"])
#         user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(detail=True, methods=["POST"], url_path="reset-password-by-token",)
#     def reset_password_by_token(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = User.objects.get(email=serializer.validated_data["email"])
#         user.set_password(serializer.validated_data["password"])
#         user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (authentication.TokenAuthentication,)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
                        
                  




class CustomObtainAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})








# urlpatterns += [
#     path("login/", CustomObtainAuthTokenView.as_view(), name="login"),
# ]


