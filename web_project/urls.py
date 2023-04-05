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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)




from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from .api_router import CustomObtainAuthTokenView, UserViewSet, MessageViewSet, ConversationViewSet

class CustomRouter(routers.SimpleRouter):
    routes = [
        
    ]

user_router = CustomRouter()
      
routers = routers.DefaultRouter()


# routers = routers.DefaultRouter()

# routers.register('chatbox', views.ChatBoxViewSet)
# routers.register('messages', views.MessagesViewSet)
# routers.register('users', views.UserViewSet)



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(routers.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path ('api-token-auth/', TokenObtainPairView.as_view()),
#     path ('api-token-refresh/', TokenRefreshView.as_view()),
#     path ('api-token-verify/', TokenVerifyView.as_view()),
    
    
# ]
app_name = "web_project"


routers.register(r"conversations", ConversationViewSet, basename="conversations")
routers.register(r"messages", MessageViewSet, basename="messages")
routers.register(r'users', UserViewSet, basename='users',)




urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
    path('token/', CustomObtainAuthTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify' )
]














    # Django Admin, use {% url 'admin:index' %}
  
   
    # User management

    
    
  
    # Your stuff: custom urls includes go here



