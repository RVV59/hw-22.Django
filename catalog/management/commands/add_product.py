# from django.core.management.base import BaseCommand
# from catalog.models import Category, Product
#
# class Command(BaseCommand):
#     help = 'Добавляет тестовые данные: категории и товары'
#
#     def handle(self, *args, **kwargs):
#         self.stdout.write("Очистка старых данных...")
#
#         # Очистка
#         Product.objects.all().delete()
#         Category.objects.all().delete()
#
#         # Добавление категорий
#         category_electronics = Category.objects.create(name="Электроника")
#         category_books = Category.objects.create(name="Книги")
#         category_clothing = Category.objects.create(name="Одежда")
#
#         # Добавление товаров
#         Product.objects.create(
#             name="Смартфон",
#             description="Современный смартфон с отличной камерой",
#             price=499.99,
#             category=category_electronics
#         )
#         Product.objects.create(
#             name="Ноутбук",
#             description="Мощный ноутбук для работы и игр",
#             price=1299.99,
#             category=category_electronics
#         )
#         Product.objects.create(
#             name="Роман 'Преступление и наказание'",
#             description="Классический роман Ф. М. Достоевского",
#             price=19.99,
#             category=category_books
#         )
#         Product.objects.create(
#             name="Футболка",
#             description="Хлопковая футболка прямого кроя",
#             price=14.99,
#             category=category_clothing
#         )
#
#         self.stdout.write(self.style.SUCCESS('✅ Товары успешно добавлены!'))
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Добавляет тестовые данные: категории и товары'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить все существующие данные перед добавлением'
        )

    def handle(self, *args, **options):
        # Очистка данных (опционально)
        if options['clear']:
            self.stdout.write("Очистка старых данных...")
            Product.objects.all().delete()
            Category.objects.all().delete()

        # Создаем категории с проверкой на существование
        categories_data = [
            {"name": "Электроника"},
            {"name": "Книги"},
            {"name": "Одежда"}
        ]

        created_categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(**cat_data)
            if created:
                created_categories.append(category.name)

        if created_categories:
            self.stdout.write(f"Созданы категории: {', '.join(created_categories)}")
        else:
            self.stdout.write("Все категории уже существуют")

        # Добавляем товары
        products_data = [
            {
                "name": "Смартфон",
                "description": "Современный смартфон с отличной камерой",
                "price": 499.99,
                "category": Category.objects.get(name="Электроника")
            },
            {
                "name": "Ноутбук",
                "description": "Мощный ноутбук для работы и игр",
                "price": 1299.99,
                "category": Category.objects.get(name="Электроника")
            },
            {
                "name": "Роман 'Преступление и наказание'",
                "description": "Классический роман Ф. М. Достоевского",
                "price": 19.99,
                "category": Category.objects.get(name="Книги")
            },
            {
                "name": "Футболка",
                "description": "Хлопковая футболка прямого кроя",
                "price": 14.99,
                "category": Category.objects.get(name="Одежда")
            }
        ]

        created_count = 0
        for prod_data in products_data:
            _, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults=prod_data
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Успешно добавлено {created_count} новых товаров!'
            )
        )