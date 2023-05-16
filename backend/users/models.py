from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username
from core.enum import Limits
from core import texts


class User(AbstractUser):
    """Модель юзера."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name',)

    username = models.CharField(
        'Уникальный юзернейм',
        validators=(validate_username,),
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        unique=True,
        blank=False,
        null=False,
        help_text=texts.USERS_HELP_UNAME,
        error_messages={'unique': texts.USERS_HELP_UNAME},
    )
    first_name = models.CharField(
        'Имя',
        max_length=Limits.MAX_LEN_USERS_CHARFIELD.value,
        blank=False,
        null=False,
        help_text=texts.USERS_HELP_FNAME,
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=Limits.MAX_LEN_EMAIL_FIELD.value,
        unique=True,
        blank=False,
        null=False,
        help_text=texts.USERS_HELP_EMAIL
    )
    avatar = models.ImageField('Аватар',
                               help_text=texts.USER_AVATAR,
                               upload_to='users/')

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email',
            )
        ]

    def __str__(self):
        return f'{self.username} {self.email}'
