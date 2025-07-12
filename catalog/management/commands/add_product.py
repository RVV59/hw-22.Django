from django.core.management.base import BaseCommand
from django.db import transaction
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми категориями и товарами'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить все существующие товары и категории перед заполнением'
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write("Очистка старых данных...")
            Product.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Данные очищены."))

        self.stdout.write("Создание категорий...")

        # 1. Создаем категории и сохраняем их объекты в словарь для быстрого доступа
        categories_to_create = ["Электроника", "Книги", "Одежда"]
        categories = {}
        for cat_name in categories_to_create:
            category, created = Category.objects.get_or_create(name=cat_name)
            categories[cat_name] = category  # Сохраняем объект, а не только имя
            if created:
                self.stdout.write(f'  - Категория "{cat_name}" создана.')

        self.stdout.write("Создание товаров...")

        # 2. Определяем данные для товаров
        products_data = [
            {
                "name": "Смартфон", "description": "Современный смартфон с отличной камерой",
                "price": 499.99, "category_name": "Электроника"
            },
            {
                "name": "Ноутбук", "description": "Мощный ноутбук для работы и игр",
                "price": 1299.99, "category_name": "Электроника"
            },
            {
                "name": "Роман 'Преступление и наказание'", "description": "Классический роман Ф. М. Достоевского",
                "price": 19.99, "category_name": "Книги"
            },
            {
                "name": "Футболка", "description": "Хлопковая футболка прямого кроя",
                "price": 14.99, "category_name": "Одежда"
            }
        ]

        created_count = 0
        # 3. Создаем товары, используя объекты категорий из нашего словаря
        for prod_data in products_data:
            category_name = prod_data.pop('category_name')
            category_obj = categories[category_name]

            # Используем defaults, чтобы обновлять данные, если товар уже существует
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                category=category_obj,
                defaults=prod_data
            )
            if created:
                created_count += 1

        if created_count > 0:
            self.stdout.write(f'  - Добавлено {created_count} новых товаров.')

        self.stdout.write(
            self.style.SUCCESS(
                '✅ Заполнение базы данных успешно завершено!'
            )
        )
