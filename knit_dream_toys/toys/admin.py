from django.contrib import admin
from .models import (
    Favorite,
    Category,
    Image,
    Toy
)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    list_display = (
        'name',
        'category',
        'slug',
        'description'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'toy'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
