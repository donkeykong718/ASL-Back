"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ASL import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
  
routers = routers.DefaultRouter()

routers.register('chatbox', views.ChatBoxViewSet)
routers.register('messages', views.MessagesViewSet)
routers.register('users', views.UserViewSet)



urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path ('api-token-auth/', TokenObtainPairView.as_view()),
    path ('api-token-refresh/', TokenRefreshView.as_view()),
    path ('api-token-verify/', TokenVerifyView.as_view()),
]
