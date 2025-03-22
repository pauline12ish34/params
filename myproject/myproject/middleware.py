from django.shortcuts import redirect

class RedirectToDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_host = "params-v1.onrender.com"  # Replace with your actual domain
        if allowed_host not in request.get_host():
            return redirect(f"https://{allowed_host}{request.path}")
        return self.get_response(request)
