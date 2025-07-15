from django.core.cache import cache
from .models import Product


def get_products_by_category(category_id):
    cache_key = f'products_category_{category_id}'
    products = cache.get(cache_key)

    if not products:
        products = Product.objects.filter(
            category_id=category_id,
            publish_status='published'
        ).select_related('category')
        cache.set(cache_key, products, 60 * 60)
    return products