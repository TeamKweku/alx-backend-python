from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Conversation, Message

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'role', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('role', 'is_staff', 'is_superuser')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_id', 'created_at')
    filter_horizontal = ('participants_id',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'sender_id', 'message_body', 'sent_at', 'conversation')
    list_filter = ('sent_at',)
    search_fields = ('message_body',)
