from rest_framework import serializers
from accounts.models import User


class ProductCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def get_photo_url(self, cat):
        request = self.context.get('request')
        photo_url = cat.image.url
        return request.build_absolute_uri(photo_url)