from django.contrib import admin

from .models import Tag, Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'context', 'author', 'get_tags', 'count_favorites']
    readonly_fields = ('count_favorites',)

    @admin.display(description='Тэги')
    def get_tags(self, obj):
        """Получаем теги."""
        return ', '.join(_.name for _ in obj.tags.all())

    @admin.display(description='Количество в избранных')
    def count_favorites(self, obj):
        """Получаем количество избранных."""
        return obj.favorites.count()
