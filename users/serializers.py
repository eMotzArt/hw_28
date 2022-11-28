from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = User
        fields = ['id', 'slug', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']

class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = '__all__'

class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    location = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'slug', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']

class UserDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id']
