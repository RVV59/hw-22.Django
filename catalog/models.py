# catalog/models.py

from django.db import models
from django.conf import settings

PUBLISH_STATUS_CHOICES = [
    ('draft', 'Черновик'),
    ('published', 'Опубликовано'),
]

class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения"
    )
    publish_status = models.CharField(
        max_length=20,
        choices=PUBLISH_STATUS_CHOICES,
        default='draft',
        verbose_name="Статус публикации"
    )

    # 2. Добавляем владельца продукта
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец"
    )

    class Meta:
        db_table = 'Product'
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
            ("can_change_product_description", "Может изменять описание продукта"),
            ("can_change_product_category", "Может изменять категорию продукта"),
        ]
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Наименование"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )

    class Meta:
        db_table = 'Category'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
