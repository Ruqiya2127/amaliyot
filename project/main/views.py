from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpRequest
from .models import Products, Category, Comment
from .form import CommentForm, ProductForm

from django.contrib.auth.decorators import login_required

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
    product = get_object_or_404(Products, id=product_id)

    context={'product':product}
    return render(request, 'main/detail.html', context)


def detail(request: HttpRequest, product_id):
    product = get_object_or_404(Products, id=product_id)
    comments = Comment.objects.filter(product_id = product_id)
    context = {'product':product, 'comments':comments}
    return render(request, 'main/detail.html', context)

def save_comment(request: HttpRequest, product_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # text= request.POST.get('text')
            form = CommentForm(data=request.POST)
            if form.is_valid():

                product = get_object_or_404(Products,  id= product_id)
                comments = Comment.objects.create(text=form.cleaned_data.get("text"), product=product, user = request.user)
            else:
                print("Harflar belgilangan miqdordan kop")
            return redirect('detail', product_id=product_id)
        else:
            return redirect('home')
    else:
        print('login qiling')
        return redirect ('home')

def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id= comment_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data= request.POST)
            if form.is_valid():
                comment.text=form.cleaned_data.get("text")
                comment.save()
                return redirect( 'detail', product_id = comment.product_id)
            else:
                form = CommentForm(initail={'text':comment.text})
            context={
                'form':form
            }
            return render(request, 'main/comment_update.html', context)
        else:
            print("login qiling")
            return redirect('home')

def delete_comment(request, comment_id):
    comment= get_object_or_404(Comment, id = comment_id)
    if request.user.is_authenticated and request.user == comment.user or request.user.is_superuser:
        product_id =comment.product.id
        if request.method == 'POST':
            comment.delete()
            return redirect('detail', product_id= product_id)
        else:
            return render(request, "main/confirm_delete.html", {"comment": comment})
    else:
        print("login qiling")
        return redirect('home')
    
def create_product(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = ProductForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                product = form.save()
                return redirect("detail", product_id=product.id)
        else:
            form = ProductForm()
        context = {
            "form": form
        }
        return render(request, "main/add_product.html", context)
    else:
        return redirect("home")

def update_product(request, product_id):

    if request.user.is_superuser:
        product = get_object_or_404(Products, pk= product_id)
        if request.method == 'POST':
            form = ProductForm(data=request.POST, files=request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect("detail", product_id= product_id)
        else:
            form = ProductForm(instance=product)
        context={
            "form": form
        }
        return render(request, "main/add_product.html", context)
    else:
        return redirect('home')
@login_required(login_url="home")
def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.user.is_superuser:
        if request.method == 'POST':
            product.delete()
            return redirect('detail', product_id=product_id)
        else:
            return render(request, 'main/delete_product.html', {'product': product} )
    else:
        return redirect('home')
