from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" и назначает ей права'

    def handle(self, *args, **options):
        try:
            content_type = ContentType.objects.get_for_model(Product)

            can_unpublish = Permission.objects.get(
                codename='can_unpublish_product',
                content_type=content_type
            )
            can_change_desc = Permission.objects.get(
                codename='can_change_product_description',
                content_type=content_type
            )
            can_change_cat = Permission.objects.get(
                codename='can_change_product_category',
                content_type=content_type
            )
            delete_product = Permission.objects.get(
                codename='delete_product',
                content_type=content_type
            )

            moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

            if created:
                self.stdout.write('Группа "Модератор продуктов" создана.')
            permissions_to_add = [
                can_unpublish,
                can_change_desc,
                can_change_cat,
                delete_product,
            ]
            moderator_group.permissions.add(*permissions_to_add)

            self.stdout.write(self.style.SUCCESS('✅ Права для группы "Модератор продуктов" успешно настроены.'))

        except Permission.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f'Ошибка: право не найдено. Выполните миграции. {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Произошла ошибка: {e}'))
