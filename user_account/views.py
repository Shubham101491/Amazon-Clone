from django.shortcuts import render
from amazon import settings


def your_account(request):
    return render(request, 'user_account/your-account.html', {"BASE_URL": settings.BASE_URL})

def login_security(request):
    return render(request, 'user_account/login-security.html', {"BASE_URL": settings.BASE_URL})
