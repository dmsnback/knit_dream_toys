from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    """Модель категорий игрушек"""

    name = models.CharField(
        'Категория',
        max_length=250,
        help_text='Напишите название категорию'
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        help_text='Напишите URL для тега'
    )

    class Meta:
        verbose_name = 'Категория',
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Toy(models.Model):
    """Модель игрушки"""

    name = models.CharField(
        'Название игрушки',
        max_length=250,
        help_text='Напишите название игрушки'
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        help_text='Напишите URL для игрушки'
    )
    description = models.TextField(
        'Описание',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='toys',
        verbose_name='Категория',
        null=True,
        blank=True,
        help_text='Выберите или добавте категорию'
    )

    class Meta:
        verbose_name = 'Игрушка',
        verbose_name_plural = 'Игрушки'

    def __str__(self):
        return self.name


class Image(models.Model):
    """Модель изображений"""
    name = models.CharField(
        'Название изображения',
        max_length=250,
        help_text='Напишите название изображения'
    )
    toy = models.ForeignKey(
        Toy,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Изображенеи игрушки',
        upload_to='toys_image/',
        help_text='Загрузите фото игрушки'
    )
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Фотография игрушки',
        verbose_name_plural = 'Фотографии игрушек'

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Модель избранного"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    toy = models.ForeignKey(
        Toy,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Игрушка'
    )

    class Meta:
        verbose_name = 'Избранное'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'toy'],
                name='unique_favorites'
            )
        ]

    def __str__(self):
        return f'Игрушка {self.toy} добавлена в избранное.'
