from django.contrib import admin
from .models import ProductCat, Product, Topping, Image, Ingredients, IngredientsUnit, IngredientsProduct, Cup, CupUnit
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCat)
class ProductCatAdmin(admin.ModelAdmin):
    pass


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientsUnit)
class IngredientsUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientsProduct)
class IngredientsProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Cup)
class CupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'size')


@admin.register(CupUnit)
class CupUnitAdmin(admin.ModelAdmin):
    pass
