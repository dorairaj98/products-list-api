from rest_framework import serializers
from .models import shop, category, product, media

class mediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = media
        fields = ['product_image']

class productSerializer(serializers.ModelSerializer):
    product_images = mediaSerializer(many=True, read_only=True)
    class Meta:
        model = product
        fields = ['id','product_name','product_images']

class categorySerializer(serializers.ModelSerializer):
    products = productSerializer(many=True, read_only=True)
    class Meta:
        model = category
        fields = ['id', 'category_name','products']