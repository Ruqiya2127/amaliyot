from django.urls import path
from .views import index, detail, product_by_category, save_comment



urlpatterns = [
    path  ('', index, name='home'),
    path('category/<int:category_id>/', product_by_category, name='product_by_category'),
    path ('product/<int:product_id>/', detail, name='detail'),
    path('add/comment/<int:product_id>/', save_comment, name='save_comment' ),
]