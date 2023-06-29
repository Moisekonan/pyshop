from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'authentification/login.html')

def register(request):
    return render(request, 'authentification/register.html')

def motdepasse_oublier(request):
    return render(request, 'authentification/forgot-password.html')

def user_profil(request):
    return render(request, 'authentification/user-profile.html')
