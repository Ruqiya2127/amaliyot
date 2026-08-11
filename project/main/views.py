from django.shortcuts import render

from django.http import Http404
from .models import Products, Category

def index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    context ={
        'products': products,
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def product_by_category(request, category_id):
    categories = Category.objects.all()
    products = Products.objects.filter(category_id= category_id)
    context={
        'products': products,
        'categories': categories
    }
    return render(request, "main/index.html", context)

def detail(request, product_id):
    product = Products.objects.get(id=product_id)

    context={'product':product}
    return render(request, 'main/detail.html', context)

    raise Http404('Product not found')