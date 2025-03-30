from django.contrib.auth import get_user_model
from django.conf import settings
from employee.models import Employee

User = get_user_model()

def get_user_from_email(email):
    """Lấy user hiện có hoặc tạo mới từ email Google"""
    try:
        # Kiểm tra nếu user đã tồn tại
        return User.objects.get(email=email)
    except User.DoesNotExist:
        # Kiểm tra nếu có nhân viên với email này nhưng chưa có tài khoản
        try:
            employee = Employee.objects.get(email=email)
            
            # Tạo username từ email
            username = email.split('@')[0]
            base_username = username
            counter = 1
            
            # Đảm bảo username duy nhất
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            # Tạo user mới
            user = User.objects.create(
                username=username,
                email=email,
                first_name=employee.first_name if hasattr(employee, 'first_name') else '',
                last_name=employee.last_name if hasattr(employee, 'last_name') else '',
                is_active=True,
                role='Employee',
                status='Active',
                employee=employee
            )
            
            return user
        except Employee.DoesNotExist:
            # Tạo user mới không liên kết với employee
            username = email.split('@')[0]
            base_username = username
            counter = 1
            
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            user = User.objects.create(
                username=username,
                email=email,
                is_active=True,
                role='Employee',
                status='Active'
            )
            
            return user