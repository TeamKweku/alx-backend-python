from django.urls import path, include
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet

# Initialize the parent router
parent_router = routers.DefaultRouter()

# Register the parent viewset
parent_router.register(r'conversations', ConversationViewSet, basename='conversation')
parent_router.register(r'messages', MessageViewSet, basename='message')

# Initialize the nested router
messages_router = routers.NestedDefaultRouter(parent_router, r'conversations', lookup='conversation')
messages_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# Generate URLs
urlpatterns = [
    path('', include(parent_router.urls)),
    path('', include(messages_router.urls)),
] 