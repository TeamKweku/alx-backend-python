from datetime import datetime, timedelta
from django.http import HttpResponseForbidden
from collections import defaultdict


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


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to store message counts per IP
        self.message_counts = defaultdict(list)
        self.max_messages = 5  # Maximum messages per minute
        self.time_window = 60  # Time window in seconds (1 minute)

    def __call__(self, request):
        # Only check POST requests (assuming these are message sends)
        if request.method == "POST":
            ip_address = self.get_client_ip(request)
            current_time = datetime.now()

            # Clean up old messages outside the time window
            self.message_counts[ip_address] = [
                timestamp
                for timestamp in self.message_counts[ip_address]
                if current_time - timestamp < timedelta(seconds=self.time_window)
            ]

            # Check if user has exceeded the rate limit
            if len(self.message_counts[ip_address]) >= self.max_messages:
                return HttpResponseForbidden(
                    f"Rate limit exceeded. Maximum {self.max_messages} messages per minute allowed."
                )

            # Add current message timestamp
            self.message_counts[ip_address].append(current_time)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
