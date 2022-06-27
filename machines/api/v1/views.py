from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from machines.models import Sensor, Timer
from .serializers import ReadingSensorSerializer, TimerSerializer


class SensorView(APIView):

    @permission_classes((AllowAny,))
    def post(self, request):
        sensor = Sensor.objects.get(serial_number=request.data.get("sensor"))
        reading_data = {"value":str(request.data.get("value")),
                        "sensor":sensor.pk}
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

