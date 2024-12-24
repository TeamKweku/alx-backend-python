from rest_framework import permissions

class IsParticipant(permissions.BasePermission):
    """Only allow participants of a conversation to access it."""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if user is a participant in the conversation
        return request.user in obj.participants_id.all()

class IsMessageParticipant(permissions.BasePermission):
    """Only allow participants of a conversation to access its messages."""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if user is a participant in the conversation that contains the message
        return request.user in obj.conversation.participants_id.all()

class IsSenderOrReadOnly(permissions.BasePermission):
    """Only allow message senders to edit their messages."""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the sender of the message
        return obj.sender_id == request.user 