from django.urls import path, include
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet

# Initialize the router
router = routers.DefaultRouter()

# Register viewsets with the router
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Generate URLs
urlpatterns = [
    path('', include(router.urls)),
] 