from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ProductViewSet, OrderViewSet, CategoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    # Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Maxsus mahsulotlar ro‘yxati (masalan, frontendda asosiy sahifa uchun)
    path('olcha/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),

    # Router orqali avtomatik generatsiya qilingan endpointlar
    path('', include(router.urls)),
]


