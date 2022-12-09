from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib import messages

def unauthenticated(view):
    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view(request, *args, **kwargs)
    return wrapper

def farmer_required(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_farmer:
            return view(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper