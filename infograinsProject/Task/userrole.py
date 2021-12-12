from django.http import HttpResponse
from django.shortcuts import redirect


def check_user_is_logged_in_or_not(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('superuser_product')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def check_superuser(allowed_supersu = []):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_supersu:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")

        return wrapper_func
    return decorator


def superuser_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "superuser":
            return view_func(request, *args, **kwargs)
    return wrapper_func