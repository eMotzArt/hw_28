from rest_framework import serializers

from ads.models import Location, Category, Advertisement


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'slug', 'name', 'lat', 'lng']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'name']

class AdvertisementSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    author = serializers.SlugRelatedField(read_only=True, slug_field='first_name')
    class Meta:
        model = Advertisement
        fields = ['id', 'slug', 'name', 'price', 'description', 'image', 'is_published', 'author', 'author_id', 'category', 'category_id']