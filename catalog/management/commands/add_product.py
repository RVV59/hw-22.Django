from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавляет тестовые данные: категории и товары'

    def handle(self, *args, **kwargs):
        self.stdout.write("Очистка существующих данных...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        category_electronics = Category.objects.create(name="Электроника")
        category_books = Category.objects.create(name="Книги")
        category_clothing = Category.objects.create(name="Одежда")

        # Создаем товары
        Product.objects.create(
            name="Смартфон",
            description="Современный смартфон с отличной камерой",
            price=499.99,
            category=category_electronics
        )
        Product.objects.create(
            name="Ноутбук",
            description="Мощный ноутбук для работы и игр",
            price=1299.99,
            category=category_electronics
        )
        Product.objects.create(
            name="Роман 'Преступление и наказание'",
            description="Классический роман Ф. М. Достоевского",
            price=19.99,
            category=category_books
        )
        Product.objects.create(
            name="Футболка",
            description="Хлопковая футболка прямого кроя",
            price=14.99,
            category=category_clothing
        )

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены!'))