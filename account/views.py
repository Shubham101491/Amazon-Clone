from django.shortcuts import render
from amazon import settings


def signin(request):
    return render(request, 'account/signin.html', {"BASE_URL": settings.BASE_URL})

def register(request):
    return render(request, 'account/register.html', {"BASE_URL": settings.BASE_URL})
