from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Room

def home(request):
    if request.user.is_authenticated:
        rooms = Room.objects.filter(user=request.user)
        return render(request, 'home.html', {'rooms': rooms})
    return render(request, 'home.html')

def login_view(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    
    username : str = request.POST.get('user')
    password : str = request.POST.get('password')

    user = authenticate(request,username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    
    data = {
        'first_name': request.POST.get('name'),
        'last_name' : request.POST.get('lastname'),
        'username'  : request.POST.get('username'),
        'email'     : request.POST.get('email'),
        'password'  : request.POST.get('password'),
        'password2' : request.POST.get('password2'),
    }

    for info in data.values():
        if info is None:
            return render(request, 'register.html')
        
    try:
        validate_email(data['email'])
    
    except:
        return render(request,'register.html')
    
    if User.objects.filter(username=data['username']).exists():
        return render(request, 'register.html')
    
    elif User.objects.filter(email=data['email']).exists():
        return render(request, 'register.html')

    elif data['password'] != data['password2']:
        return render(request, 'register.html')

    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
    )

    user.save()
    return redirect('home')