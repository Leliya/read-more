from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators

from core.enum import Limits, Regex
from core import texts

User = get_user_model()


class Tag(models.Model):
    """Модель тегов."""

    name = models.CharField(
        'Наименование',
        max_length=Limits.MAX_LEN_TAG.value,
        unique=True,
        help_text=texts.WARNING_LIMIT_CHAR,
    )
    slug = models.SlugField('URL', unique=True,
                            validators=[validators.validate_slug],)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Post(models.Model):
    """Параметры добавления новых постов."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    title = models.CharField('Заголовок',
                             max_length=100)

    context = models.TextField('Контекст')

    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        constraints = (
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='unique_author_post',
            ),
        )


class Favorite(models.Model):
    """Модель избранного."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Пользователь',
        related_name = 'favorites'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name = 'favorites'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'post',),
                name='unique_user_post',
            ),
        )

    def __str__(self):
        return (
            f'Пользователь {self.user} добавил {self.post.title} в избранное'
        )
