from django.shortcuts import render
from amazon import settings


def your_account(request):
    return render(request, 'user_account/your-account.html', {"BASE_URL": settings.BASE_URL})


def your_addresses(request):
    return render(request, 'user_account/address/your-addresses.html', {"BASE_URL": settings.BASE_URL})


def new_address(request):
    return render(request, 'user_account/address/new-address.html', {"BASE_URL": settings.BASE_URL})
