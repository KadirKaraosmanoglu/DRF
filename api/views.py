from rest_framework import generics
from django.contrib.auth.models import User
from django.db.models import Case, When, Q, BooleanField

from .models import Product, Category, Slider, Favorites
from .serializers import RegisterSerializer, ProductFavoriteSerializer, CategoryListSerializer, \
    ProductSerializer, \
    CategoryDetailPostSerializer, \
    SliderSerializer, FavoritesSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailPostSerializer


class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductFavoriteSerializer

    def get_queryset(self):
        return Product.objects.prefetch_related('favorite').annotate(
            isFavorite=Case(When(Q(favorite__user=self.request.user), then=True),
                            default=False,
                            output_field=BooleanField()))


class SliderCreateDetailAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class FavoritesCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductForCategoryListAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductFavoriteSerializer

    def get_queryset(self):
        return Product.objects.prefetch_related('favorite').filter(category=self.kwargs['pk']).annotate(
            isFavorite=Case(When(Q(favorite__user=self.request.user), then=True),
                            default=False,
                            output_field=BooleanField()))


class UserRegisterAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
