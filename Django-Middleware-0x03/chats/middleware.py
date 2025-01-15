from datetime import datetime
from django.http import HttpResponseForbidden


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current user (anonymous if not authenticated)
        user = request.user if hasattr(request, "user") else "AnonymousUser"

        # Log the request
        with open("requests.log", "a") as log_file:
            log_file.write(f"{datetime.now()} - User: {user} - Path: {request.path}\n")

        # Call the next middleware/view
        response = self.get_response(request)

        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()
        # Check if time is between 9 AM and 6 PM
        if current_time.hour < 9 or current_time.hour >= 18:
            return HttpResponseForbidden(
                "Access to chat is only allowed between 9 AM and 6 PM"
            )

        response = self.get_response(request)
        return response
