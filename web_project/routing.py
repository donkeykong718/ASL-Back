from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from ASL import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_box_name>\w+)/$', consumers.ChatRoomConsumer),
]


application = ProtocolTypeRouter( 
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)
