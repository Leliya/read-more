from rest_framework import decorators, permissions, response, status, viewsets
from rest_framework.generics import get_object_or_404

from .serializers import TagSerializer
from .models import Tag, Post, Favorite
from .permissions import AuthorOrReadOnly
from .serializers import (PostWriteSerializer, PostReadSerializer,
                          AddFavoritePostSerializer)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для отображения тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для отображения постов.
    Для запросов на чтение используется PostReadSerializer
    Для запросов на изменение используется PostWriteSerializer"""

    queryset = Post.objects.all()
    permission_classes = (AuthorOrReadOnly,)

    def get_serializer_class(self):
        if self.request and self.request.method in ('POST', 'PUT', 'PATCH'):
            return PostWriteSerializer
        return PostReadSerializer

    @decorators.action(
        detail=True,
        methods=['POST', 'DELETE'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def favorite(self, request, post_id):
        user = request.user
        data = {'user': user.id,
                'post': post_id}
        serializer = AddFavoritePostSerializer(data=data,
                                               context={'request': request})
        if request.method == 'POST':
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(serializer.data,
                                    status=status.HTTP_201_CREATED)
        get_object_or_404(
            Favorite, user=user, post=get_object_or_404(Post, id=post_id)
        ).delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
