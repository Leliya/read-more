from django.urls import path, include
from rest_framework import routers

from users.views import CustomUserViewSet
from blog.views import TagViewSet, PostViewSet



router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
