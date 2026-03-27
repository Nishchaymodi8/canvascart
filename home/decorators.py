from django.contrib import messages
from django.shortcuts import redirect

def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            messages.error(request, "Please login first")
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper