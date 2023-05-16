from djoser.views import UserViewSet

from .models import User
from .serializers import UsersSerializer


class CustomUserViewSet(UserViewSet):
    """Вьюсет для кастомной модели пользователя."""

    queryset = User.objects.all()
    serializer_class = UsersSerializer
