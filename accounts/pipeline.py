def set_user_defaults(backend, strategy, details, user=None, *args, **kwargs):
    if user and user.is_active == False:
        user.is_active = True
        user.status = 'Active'
        user.save()


def associate_by_email(backend, details, user=None, *args, **kwargs):
    """
    Custom pipeline function to associate a Google OAuth account with an existing user
    based on email address.
    """
    if user:
        return {'is_new': False}
    
    email = details.get('email')
    if email:
        from .utils import get_user_from_email
        user = get_user_from_email(email)
        if user:
            return {'is_new': False, 'user': user}
    
    return None

def set_user_details(backend, strategy, details, user=None, *args, **kwargs):
    """Update user details from social auth information"""
    if not user:
        return
    
    changed = False
    
    # Cập nhật thông tin từ Google nếu chưa có
    if details.get('fullname') and not (user.first_name and user.last_name):
        full_name = details.get('fullname')
        if ' ' in full_name:
            user.first_name = full_name.split(' ')[0]
            user.last_name = ' '.join(full_name.split(' ')[1:])
        else:
            user.first_name = full_name
        changed = True
    
    if details.get('first_name') and not user.first_name:
        user.first_name = details.get('first_name')
        changed = True
    
    if details.get('last_name') and not user.last_name:
        user.last_name = details.get('last_name')
        changed = True
    
    # Lưu thay đổi nếu có
    if changed:
        user.save()