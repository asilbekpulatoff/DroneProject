from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path_info.startswith('/auth/'):  # Adjust the login URL as needed
            return redirect(reverse('login'))  # Redirect to your login URL

        response = self.get_response(request)
        return response
