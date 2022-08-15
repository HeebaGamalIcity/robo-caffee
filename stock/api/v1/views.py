from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, SAFE_METHODS
from lookups.models import Ingredients, Cup
from lookups.api.v1.serializers import IngredientsSerializer, CupSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IngredientStock(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request):
        response_data = {
            "state": True,
            "message": "Ok",
            "data": []
        }
        lang = request.headers["lang"]
        ingredients = Ingredients.objects.all()
        serializer = IngredientsSerializer(instance=ingredients, lang=lang, context={"request": request}, many=True)
        response_data["data"] = serializer.data
        for r in response_data["data"]:
            del r["topping"]
            del r["unit"]
            del r["product"]
        return Response(data=response_data, status=status.HTTP_200_OK)


class CupStock(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request):
        response_data = {
            "state": True,
            "message": "Ok",
            "data": []
        }
        cups = Cup.objects.all()
        serializer = CupSerializer(instance=cups, many=True)
        response_data["data"] = serializer.data
        for r in response_data["data"]:
            del r["unit"]
        return Response(data=response_data, status=status.HTTP_200_OK)
