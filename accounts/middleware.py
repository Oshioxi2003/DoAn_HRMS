from .models import SystemLog

class SystemLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Log only POST/PUT/DELETE actions by authenticated users
        if request.method in ['POST', 'PUT', 'DELETE'] and request.user.is_authenticated:
            # Exclude some paths like admin actions, static files, etc.
            excluded_paths = ['/admin/jsi18n/', '/static/', '/media/']
            if not any(request.path.startswith(path) for path in excluded_paths):
                SystemLog.objects.create(
                    user=request.user,
                    action=f"{request.method} {request.path}",
                    details=request.POST.get('action', ''),
                    ip=self._get_client_ip(request),
                    user_agent=request.META.get('HTTP_USER_AGENT', '')
                )
        
        return response
    
    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip