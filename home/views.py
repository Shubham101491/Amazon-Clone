from django.shortcuts import render
from amazon import settings


def home(request):
    return render(request, 'home/home.html', {"BASE_URL": settings.BASE_URL})
