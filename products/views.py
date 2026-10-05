from django.shortcuts import render, get_object_or_404
from .models import Products


def shop(request):
    products = Products.objects.all()
    return render(request, 'products/shop.html', {'products': products})


def product_details(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'products/product-details.html', {'product': product})