from django.contrib.auth.models import User

from rest_framework import serializers
from .models import ChatBox, Messages


class MessagesSerializer(serializers.ModelSerializer):
  chat_room = serializers.ReadOnlyField(source='chat_room.name')
  class Meta:
        model = Messages
        fields = ('id', 'chat_name', 'user', 'message', 'timestamp', 'chat_room')

class ChatBoxSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    users = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    messages =  serializers.PrimaryKeyRelatedField(many=True, read_only=True )
    class Meta:
        model = ChatBox
        fields = '__all__'
        
  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
  
class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('id', 'chat_name', 'user', 'message', 'timestamp',)
