from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('products-cat', views.ProductCatList.as_view()),
    path('', views.LookupsList.as_view()),
]