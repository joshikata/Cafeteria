def user_role(request):
    if request.user.is_authenticated:
        return {
            'user_role': 'Encargado' if request.user.is_staff else 'Cliente',
            'username': request.user.username,
        }
    return {}
