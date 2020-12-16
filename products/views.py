from django.shortcuts import render
from amazon import settings


def product_detail(request):
    return render(request, 'products/product-detail.html', {"BASE_URL": settings.BASE_URL})
