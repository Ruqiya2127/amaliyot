from django.shortcuts import render, redirect

from django.http import HttpRequest
from .models import Products, Category, Comment

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


def detail(request: HttpRequest, product_id):
    product = Products.objects.get(id=product_id)
    comments = Comment.objects.filter(product_id = product_id)
    context = {'product':product, 'comments':comments}
    return render(request, 'main/detail.html', context)

def save_comment(request: HttpRequest, product_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            text= request.POST.get('text')
            product = Products.objects.get(id= product_id)
            comments = Comment.object.create(text=text, product=product, user = request.user)
            return redirect('detail', product_id=product_id)
        else:
            return redirect('home')
    else:
        print('login qiling')
        return redirect ('home')