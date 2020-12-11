from django.shortcuts import render
from amazon import settings


def return_order(request):
    return render(request, 'order/return-order.html', {"BASE_URL": settings.BASE_URL})


def cancelled_order(request):
    return render(request, 'order/cancelled-order.html', {"BASE_URL": settings.BASE_URL})

def open_order(request):
    return render(request, 'order/open-order.html', {"BASE_URL": settings.BASE_URL})

def buy_again(request):
    return render(request, 'order/buy-again.html', {"BASE_URL": settings.BASE_URL})
