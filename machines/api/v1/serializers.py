from rest_framework import serializers
from machines.models import ReadingSensor, Timer


class ReadingSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingSensor
        fields = '__all__'


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'
