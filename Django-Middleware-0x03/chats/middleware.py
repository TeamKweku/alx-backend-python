from datetime import datetime


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
