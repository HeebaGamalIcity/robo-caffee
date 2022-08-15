from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from lookups.models import ProductCat, Product, Image, Ingredients, IngredientsProduct
from .serializers import ProductCatSerializer, ProductSerializer, ImageSerializer, IngredientsSerializer


class ProductList(ListView):
    model = Product


class ProductCatList(ListView):
    model = ProductCat


def get_cat(cat, request):
    lang = request.headers["lang"]
    products = Product.objects.filter(product_cat=cat.pk)
    cat_serializer = ProductCatSerializer(instance=cat, lang=lang, context={"request": request})
    product_serializer = ProductSerializer(instance=products, many=True, lang=lang, context={"request": request})
    cat_data = {"catInfo": cat_serializer.data,
                "products": product_serializer.data}
    main_cat_id = main_cat_product(cat)
    # for p in product_serializer.data:
    #     toppings_list = []
    #     toppings_product =
    #     for t in p['toppings']:
    #         topping_query = Ingredients.objects.get(pk=t)
    #         topping_serializer = ToppingSerializer(instance=topping_query, lang=lang, context={"request": request})
    #         toppings_list.append(topping_serializer.data)
    #     p['toppings'] = toppings_list
    #     p['mainCat'] = main_cat_id

    return cat_data


def main_cat_product(cat):
    if cat.parent_cat is None:
        return cat.pk
    else:
        return main_cat_product(cat.parent_cat)


class LookupsList(APIView):

    @permission_classes((AllowAny,))
    def get(self, request):
        response_data = {
            "state": True,
            "message": "Ok",
            "data": {"catList": []}
        }
        cats = ProductCat.objects.filter(parent_cat=None)
        for c in cats:
            sub_cats = ProductCat.objects.filter(parent_cat=c.pk)
            if not len(sub_cats):
                response_data["data"]["catList"].append(get_cat(c, request))
                response_data["data"]["catList"][-1]["subCat"] = []
            else:
                cat_serializer = ProductCatSerializer(instance=c, context={"request": request})
                cat_data = {"catInfo": cat_serializer.data,
                            "subCat": []}
                for s in sub_cats:
                    cat_data["subCat"].append(get_cat(s, request))
                response_data["data"]["catList"].append(cat_data)
        images = Image.objects.all()
        images_serializer = ImageSerializer(instance=images, many=True, context={"request": request})
        response_data["data"]["images"] = images_serializer.data
        return Response(data=response_data, status=status.HTTP_200_OK)
