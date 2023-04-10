from rest_framework import serializers
from django.contrib.auth import get_user_model
from chats.models import Message, Conversation


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user






class MessageSerializer(serializers.ModelSerializer):
    from_user = serializers.SerializerMethodField()
    conversation = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = (
            "id",
            "conversation",
            "from_user",
            
            "content",
            "timestamp",
            "read",
        )

    def get_conversation(self, obj):
        return str(obj.conversation.id)

    def get_from_user(self, obj):
        return UserSerializer(obj.from_user).data
   

class ConversationSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ("id", "name", "category",  "last_message")

    def get_last_message(self, obj):
        messages = obj.messages.all().order_by("-timestamp")
        if not messages.exists():
            return None
        message = messages[0]
        return MessageSerializer(message).data


  
              
