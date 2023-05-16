from django.db import models, transaction
from django.shortcuts import get_object_or_404
from rest_framework import (exceptions, fields, relations, serializers,
                            status, validators)

from .models import Post, Tag, Favorite
from core import texts
from users.serializers import UsersSerializer


class TagSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Tag."""

    class Meta:
        model = Tag
        fields = '__all__'


class PostReadSerializer(serializers.ModelSerializer):
    """ Сериализатор для возврата постов."""

    tags = TagSerializer(many=True, read_only=True)
    author = UsersSerializer(read_only=True)
    is_favorited = fields.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'tags', 'title', 'author', 'context', 'is_favorited',
        )

    def get_is_favorited(self, obj):
        """Проверка - находится ли пост в избранном."""
        request = self.context.get('request')
        return (request and request.user.is_authenticated
                and request.user.favorites.filter(post=obj).exists())


class PostWriteSerializer(serializers.ModelSerializer):
    """ Сериализатор для создание постов."""

    tags = relations.PrimaryKeyRelatedField(queryset=Tag.objects.all(),
                                            many=True)
    author = UsersSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'context', 'tags', 'author')
        read_only_fields = ('author',)

    @transaction.atomic
    def create(self, validated_data):
        tags = validated_data.pop('tags')
        author = self.context.get('request').user
        post = Post.objects.create(author=author, **validated_data)
        post.save()
        post.tags.set(tags)
        return post

    @transaction.atomic
    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        instance.tags.clear()
        instance.tags.set(tags)
        return super().update(instance, validated_data)

    def validate_tags(self, value):
        """Проверяем на наличие уникального тега."""
        tags = value
        if not tags:
            raise exceptions.ValidationError(
                {'tags': texts.TAG_ERROR}
            )
        tags_list = []
        for tag in tags:
            if tag in tags_list:
                raise exceptions.ValidationError(
                    {'tags': texts.TAG_UNIQUE_ERROR}
                )
            tags_list.append(tag)
        return value

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return PostReadSerializer(instance, context=context).data


class ShowPostAddedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post.
    Определён укороченный набор полей для некоторых эндпоинтов."""

    class Meta:
        model = Post
        fields = ('id', 'title')


class AddFavoritePostSerializer(serializers.ModelSerializer):
    """Сериализатор добавления постов в избранное."""

    class Meta:
        model = Favorite
        fields = ('user', 'post')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=['user', 'post'],
                message=texts.IN_FAVORITE
            )
        ]

    def to_representation(self, instance):
        request = self.context.get('request')
        return ShowPostAddedSerializer(
            instance.post,
            context={'request': request}
        ).data