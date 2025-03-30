from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from functools import wraps
from .models import Permission
from django.contrib import messages

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return _wrapped_view
    return decorator

def admin_required(view_func):
    return role_required(['Admin'])(view_func)

def hr_required(view_func):
    return role_required(['HR', 'Admin'])(view_func)

def manager_required(view_func):
    return role_required(['Manager', 'HR', 'Admin'])(view_func)

def employee_required(view_func):
    return role_required(['Employee', 'Manager', 'HR', 'Admin'])(view_func)

def check_module_permission(module, required_permission='View'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Superusers have all permissions
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            
            # Special case for employee_evaluations - check if user is the employee being viewed
            if view_func.__name__ == 'employee_evaluations' and 'employee_id' in kwargs:
                employee_id = kwargs.get('employee_id')
                if request.user.employee and str(request.user.employee.employee_id) == str(employee_id):
                    return view_func(request, *args, **kwargs)
            
            # Check if user has the required permission for the module
            try:
                permission = Permission.objects.get(role=request.user.role, module=module)
                if permission.access_right == 'All' or permission.access_right == required_permission:
                    return view_func(request, *args, **kwargs)
            except Permission.DoesNotExist:
                # If no permission record exists, check if user is admin or HR
                if request.user.role in ['Admin', 'HR']:
                    return view_func(request, *args, **kwargs)
                    
                # Add a message before denying permission
                messages.error(request, 
                    f"You don't have {required_permission} permission for the {module} module.")
            
            raise PermissionDenied
        return _wrapped_view
    return decorator
