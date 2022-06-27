from rest_framework import serializers
from lookups.models import ProductCat, Product, Topping, Image


class ProductCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCat
        fields = '__all__'

    def __init__(self, lang='en', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang

    def to_representation(self, instance):
        data = super(ProductCatSerializer, self).to_representation(instance)
        if self.lang == 'ar':
            data["name"] = data["ar_name"]
        else:
            data["name"] = data["en_name"]
        del data["ar_name"]
        del data["en_name"]
        return data

    def get_photo_url(self, cat):
        request = self.context.get('request')
        photo_url = cat.image.url
        return request.build_absolute_uri(photo_url)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, lang='en', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang


    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        if self.lang == 'ar':
            data["name"] = data["ar_name"]
        else:
            data["name"] = data["en_name"]
        del data["ar_name"]
        del data["en_name"]
        return data

    def get_photo_url(self, product):
        request = self.context.get('request')
        photo_url = product.image.url
        return request.build_absolute_uri(photo_url)



class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

    def __init__(self, lang='en', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang

    def to_representation(self, instance):
        data = super(ToppingSerializer, self).to_representation(instance)
        if self.lang == 'ar':
            data["name"] = data["ar_name"]
        else:
            data["name"] = data["en_name"]
        del data["ar_name"]
        del data["en_name"]
        return data

    def get_photo_url(self, topping):
        request = self.context.get('request')
        photo_url = topping.image.url
        return request.build_absolute_uri(photo_url)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def get_photo_url(self, image):
        request = self.context.get('request')
        photo_url = image.image.url
        return request.build_absolute_uri(photo_url)
