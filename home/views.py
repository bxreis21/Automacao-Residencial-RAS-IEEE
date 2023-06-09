from django.shortcuts import render
from .models import Room

def home(request):
    if request.user.is_authenticated:
        rooms = Room.objects.filter(user=request.user)
        return render(request, 'home.html', {'rooms': rooms})
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')