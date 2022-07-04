from rest_framework import serializers
from machines.models import ReadingSensor, Timer, Unit


class ReadingSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingSensor
        fields = '__all__'


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('ar_name', 'en_name', 'image')

    def __init__(self, lang='en', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang

    def to_representation(self, instance):
        data = super(UnitSerializer, self).to_representation(instance)
        if self.lang == 'ar':
            data["name"] = data["ar_name"]
        else:
            data["name"] = data["en_name"]
        del data["ar_name"]
        del data["en_name"]
        return data

    def get_photo_url(self, unit):
        request = self.context.get('request')
        photo_url = unit.image.url
        return request.build_absolute_uri(photo_url)
