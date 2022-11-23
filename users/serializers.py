from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = User
        fields = ['id', 'slug', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']
