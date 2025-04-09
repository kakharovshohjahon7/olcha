from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, ProductViewSet, OrderViewSet, CategoryViewSet, CommentCreateView, CommentListView, \
    CommentDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('categories', CategoryViewSet, basename='categories')


class CachedCommentListView:
    pass


urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/comments/', CommentCreateView.as_view(), name='comment-create'),
    # path('api/comments/cached/', CachedCommentListView.as_view(), name='cached-comment-list'),
    path('api/comments/', CommentListView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    path('olcha/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),

    path('', include(router.urls)),
]

