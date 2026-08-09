from django.urls import path
from .views import index, detail



urlpatterns = [
    path  ('', index, name='home'),
    path ('product/<int:product_id>/', detail, name='detail'),
]