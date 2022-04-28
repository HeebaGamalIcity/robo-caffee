from django.views.generic.list import ListView
from lookups.models import ProductCat, Product

class ProductList(ListView):
    model = Product


class ProductCatList(ListView):
    model = ProductCat

