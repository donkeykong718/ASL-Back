from django.contrib.auth.models import User

from rest_framework import serializers
from .models import ChatBox, Messages


class ChatBoxSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = ChatBox
        fields = ('id', 'name', 'users', 'messages')

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('id', 'chat_box', 'user', 'message', 'timestamp')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'products')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
