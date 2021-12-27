from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Product, Category, Slider, Favorites


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductFavoriteSerializer(serializers.ModelSerializer):
    isFavorite = serializers.SerializerMethodField('_favori')

    def _favori(self, object):
        return object.isFavorite

    class Meta:
        model = Product
        fields = ['name', 'description', 'isFavorite', 'price', 'category']


class CategoryListSerializer(serializers.ModelSerializer):
    description = serializers.CharField(write_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class CategoryDetailPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['image', 'productId']


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['productId']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Parolalar eşleşmedi"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
