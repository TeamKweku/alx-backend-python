from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    full_name = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=True)
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value

    class Meta:
        model = User
        fields = ('user_id', 'email', 'first_name', 'last_name', 
                 'phone_number', 'role', 'created_at', 'full_name', 'password')
        read_only_fields = ('user_id', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model."""
    sender = UserSerializer(source='sender_id', read_only=True)
    message_preview = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()
    
    def get_message_preview(self, obj):
        return obj.message_body[:50] + '...' if len(obj.message_body) > 50 else obj.message_body
    
    def get_formatted_date(self, obj):
        return obj.sent_at.strftime("%Y-%m-%d %H:%M:%S")
    
    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty")
        return value

    class Meta:
        model = Message
        fields = ('message_id', 'sender', 'message_body', 
                 'sent_at', 'conversation', 'message_preview', 'formatted_date')
        read_only_fields = ('message_id', 'sent_at')

class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model with nested messages."""
    participants = UserSerializer(source='participants_id', many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    last_message = serializers.SerializerMethodField()
    participant_count = serializers.SerializerMethodField()
    
    def get_last_message(self, obj):
        last_msg = obj.messages.order_by('-sent_at').first()
        return MessageSerializer(last_msg).data if last_msg else None
    
    def get_participant_count(self, obj):
        return obj.participants_id.count()
    
    def validate_participants_id(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("A conversation must have at least 2 participants")
        return value

    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants', 'messages', 
                 'created_at', 'last_message', 'participant_count')
        read_only_fields = ('conversation_id', 'created_at')

class ConversationCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new conversation."""
    participants_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=True
    )
    initial_message = serializers.CharField(write_only=True, required=False)
    
    def validate(self, data):
        if len(data.get('participants_id', [])) < 2:
            raise serializers.ValidationError({
                "participants_id": "A conversation must have at least 2 participants"
            })
        return data
    
    class Meta:
        model = Conversation
        fields = ('conversation_id', 'participants_id', 'initial_message')
        read_only_fields = ('conversation_id',)

class MessageCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a new message."""
    message_body = serializers.CharField(required=True)
    
    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty")
        if len(value) > 1000:
            raise serializers.ValidationError("Message body cannot exceed 1000 characters")
        return value.strip()

    class Meta:
        model = Message
        fields = ('message_id', 'sender_id', 'message_body', 
                 'conversation')
        read_only_fields = ('message_id',) 