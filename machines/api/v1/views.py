from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from machines.models import Sensor, Timer, Unit
from .serializers import ReadingSensorSerializer, TimerSerializer, UnitSerializer
import random


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


class SensorView(APIView):

    @permission_classes((AllowAny,))
    def get(self, request):
        sensor = Sensor.objects.get(serial_number=request.data.get("sensor"))
        reading_data = {"value": str(request.data.get("value")),
                        "sensor": sensor.pk}
        serializer = ReadingSensorSerializer(data=reading_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": 1}, status=status.HTTP_200_OK)
        return Response(data={"message": 0}, status=status.HTTP_400_BAD_REQUEST)


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
        d['totalCups'] = random.randint(0, 100)
        d['availableCups'] = random.randint(0, 75)
        d['totalGrad'] = random.randint(0, 100)
        d['availableGrad'] = random.randint(0, 75)
    response_data['data'] = unit_data.data
    return Response(data=response_data, status=status.HTTP_200_OK)



