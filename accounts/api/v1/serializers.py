from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    userType = serializers.IntegerField(source='user_type')
    class Meta:
        model = User
        fields = ("email", "userType", "image", "firstName", "lastName")

    def get_photo_url(self, cat):
        request = self.context.get('request')
        photo_url = cat.image.url
        return request.build_absolute_uri(photo_url)
