from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    class Meta:
        model = User
        fields = ('user_id', 'email', 'first_name', 'last_name', 
                 'phone_number', 'role', 'created_at')
        read_only_fields = ('user_id', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model."""
    sender = UserSerializer(source='sender_id', read_only=True)
    
    class Meta:
        model = Message
        fields = ('message_id', 'sender', 'message_body', 
                 'sent_at', 'conversation')
        read_only_fields = ('message_id', 'sent_at')

class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model with nested messages."""
    participants = UserSerializer(source='participants_id', many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants', 'messages', 
                 'created_at')
        read_only_fields = ('conversation_id', 'created_at')

class ConversationCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new conversation."""
    participants_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=True
    )
    
    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants_id')
        read_only_fields = ('conversation_id',)

class MessageCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new message."""
    class Meta:
        model = Message
        fields = ('message_id', 'sender_id', 'message_body', 
                 'conversation')
        read_only_fields = ('message_id',) 