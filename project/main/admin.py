from django.contrib import admin

from .models import Products, Category, Comment

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Comment)
