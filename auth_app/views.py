from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_login(request):
    return render(request, 'home_login.html')

def home_logout(request):
    return render(request, 'home_logout.html')

def home_register(request):
    return render(request, 'home_register.html')

@login_required
def welcome(request):
    return render(request, 'welcome.html')


from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hello, {request.user.username}")
    else:
        return HttpResponse("Hello, anonymous user")
    
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return HttpResponse(f"Welcome to dashboard, {request.user.username}")