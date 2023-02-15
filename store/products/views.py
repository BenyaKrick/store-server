from django.shortcuts import render
from products.models import ProductCategory, Product, Basket
from users import User


def index(request):
    context = {'title': 'Test Title',
               'is_promotion': True,
               }

    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Store - Каталог',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)

def basket_ad(request, product_id):
    pass
