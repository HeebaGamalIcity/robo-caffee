from django.urls import path

# importing views from views..py
from . import views

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('products-cat', views.ProductCatList.as_view()),
]