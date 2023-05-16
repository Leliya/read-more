from djoser.views import UserViewSet
from django.http import HttpResponse

from .models import User
from .serializers import UsersSerializer


class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""

    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.set_cookie('mycookie', 'myvalue', httponly=True)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.set_cookie('mycookie', 'myvalue', httponly=True)
        return response