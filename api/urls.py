from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('products', views.ProductCreateAPIView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories', views.CategoryListCreateAPIView.as_view(), name='categories'),
    path('categories/<int:pk>', views.CategoryDetailAPIView.as_view(), name='category-detail'),
    path('sliders', views.SliderCreateDetailAPIView.as_view(), name='sliders'),
    path('favorite', views.FavoritesCreateAPIView.as_view(), name='favorite'),
    path('users/login', obtain_auth_token, name='user-login'),
    path('users/register', views.UserRegisterAPIView.as_view(), name='user-register'),
    path('categories/<int:pk>/products', views.ProductForCategoryListAPIView.as_view(),
         name='products-for-category'),
]
