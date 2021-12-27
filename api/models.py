from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=48, unique=True)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=48)
    description = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'category'], name='uniqCategoryProduct')
        ]


class Slider(models.Model):
    image = models.CharField(max_length=128)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['image', 'productId'], name='uniqImageProduct')
        ]


class Favorites(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorite')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['productId', 'user'], name='uniqFavorites')
        ]
