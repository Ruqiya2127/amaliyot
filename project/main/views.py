from django.shortcuts import render, redirect

from django.http import HttpRequest
from .models import Products, Category, Comment
from .form import CommentForm

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
            # text= request.POST.get('text')
            form = CommentForm(data=request.POST)
            if form.is_valid():

                product = Products.objects.get(id= product_id)
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
    comment = Comment.objects.get(id= comment_id)
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
    comment= Comment.objects.get(id = comment_id)
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