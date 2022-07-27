import random

from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from lookups.api.v1.serializers import IngredientsSerializer, CupUnitSerializer
from lookups.models import IngredientsUnit, Ingredients, Cup, CupUnit
from machines.models import Sensor, Timer, Unit
from reports.models import ReportRefillCup, ReportRefillIngredient
from .serializers import ReadingSensorSerializer, UnitSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class SensorView(APIView):

    @permission_classes((AllowAny,))
    def post(self, request):
        sensor = Sensor.objects.get(serial_number=request.data.get("sensor"))
        reading_data = {"value": str(request.data.get("value")),
                        "sensor": sensor.pk}
        serializer = ReadingSensorSerializer(data=reading_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": 1}, status=status.HTTP_200_OK)
        return Response(data={"message": 0}, status=status.HTTP_400_BAD_REQUEST)


class UnitView(APIView):

    @permission_classes((AllowAny,))
    def get(self, request):
        lang = request.headers["lang"]
        response_data = {
            "state": True,
            "message": "Ok",
            "data": {"catList": []}
        }
        units = Unit.objects.all()
        serializer = UnitSerializer(instance=units, many=True, lang=lang, context={"request": request})
        response_data["data"] = serializer.data
        return Response(data=response_data, status=status.HTTP_200_OK)


class TimerView(APIView):

    @permission_classes((AllowAny,))
    def post(self, request):
        try:
            timer = Timer.objects.get(serial_number=request.data.get("timer"))
            timer.value = request.data.get("value")
            timer.save()
            return Response(data={"message": 1}, status=status.HTTP_200_OK)
        except:
            return Response(data={"message": 0}, status=status.HTTP_400_BAD_REQUEST)


class CupUnitView(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request, operation, unit_id):
        response_data = {
            "state": True,
            "message": "Ok",
            "data": []
        }
        if operation == "show":
            cups = CupUnit.objects.filter(unit=unit_id)
            for c in cups:
                cup_obj = Cup.objects.get(pk=c.pk)
                cup_data = CupUnitSerializer(instance=c)
                temp = cup_data.data
                temp['size'] = cup_obj.size
                del temp['unit']
                del temp['cup']
                response_data['data'].append(temp)
        return Response(data=response_data, status=status.HTTP_200_OK)

    def post(self, request, operation, unit_id):
        response_data = {
            "state": True,
            "message": "Ok",
        }
        if operation == 'refill':
            for c in request.data.get("cups"):
                cup_unit_obj = CupUnit.objects.get(cup=c["id"], unit=unit_id)
                unit = Unit.objects.get(pk=unit_id)
                cup = Cup.objects.get(pk=c["id"])
                report = ReportRefillCup(user=request.user, unit=unit, cup=cup,
                                                before=cup_unit_obj.current_tank_size, after=c["value"])
                cup_unit_obj.current_tank_size = c["value"]
                cup_unit_obj.save()
                report.save()
        return Response(data=response_data, status=status.HTTP_200_OK)


class IngredientUnitView(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request, operation, unit_id):
        response_data = {
            "state": True,
            "message": "Ok",
            "data": []
        }
        if operation == "show":
            lang = request.headers["lang"]
            ingredients = IngredientsUnit.objects.filter(unit=unit_id)
            for i in ingredients:
                ingredient_obj = Ingredients.objects.get(pk=i.ingredient.pk)
                ingredient_data = IngredientsSerializer(instance=ingredient_obj, lang=lang, context={"request": request})
                temp = ingredient_data.data
                temp['maxTankSize'] = i.max_tank_size
                temp['minTankSize'] = i.min_tank_size
                temp['currentTankSize'] = i.current_tank_size
                del temp['unit']
                del temp['product']
                response_data['data'].append(temp)
        return Response(data=response_data, status=status.HTTP_200_OK)

    def post(self, request, operation, unit_id):
        response_data = {
            "state": True,
            "message": "Ok",
        }
        if operation == 'refill':
            for i in request.data.get("ingredients"):
                ingredient_unit_obj = IngredientsUnit.objects.get(ingredient=i["id"], unit=unit_id)
                unit = Unit.objects.get(pk=unit_id)
                ingredient = Ingredients.objects.get(pk=i["id"])
                report = ReportRefillIngredient(user=request.user, unit=unit, ingredient=ingredient,
                                                before=ingredient_unit_obj.current_tank_size, after=i["value"])
                ingredient_unit_obj.current_tank_size = i["value"]
                ingredient_unit_obj.save()
                report.save()

        return Response(data=response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def home(request):
    response_data = {
        "state": True,
        "message": "Ok",
        "data": {}
    }
    lang = request.headers["lang"]
    units = Unit.objects.all()
    unit_data = UnitSerializer(instance=units, many=True, lang=lang, context={"request": request})
    for d in unit_data.data:
        d['totalCups'] = 100
        d['availableCups'] = random.randint(0, 75)
        d['totalGrad'] = 100
        d['availableGrad'] = random.randint(0, 75)
        d['orders'] = 12345
        d['transactions'] = 20145
    response_data['data'] = unit_data.data
    return Response(data=response_data, status=status.HTTP_200_OK)
