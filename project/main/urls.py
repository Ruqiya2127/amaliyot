from django.urls import path
from .views import (index, detail, product_by_category, save_comment, update_comment, delete_comment, create_product, update_product, delete_product)



urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', product_by_category, name='product_by_category'),
    path ('product/<int:product_id>/', detail, name='detail'),
    path('add/comment/<int:product_id>/', save_comment, name='save_comment' ),
    path('update/comment/<int:comment_id>/', update_comment, name='update_comment'),
    path('delete/comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('book/add/', create_product, name='add_product'),
    path('book/<int:product_id>/update/', update_product, name='update_product'),
    path('book/<int:product_id>/delete/', delete_product, name='delete_product'),
]