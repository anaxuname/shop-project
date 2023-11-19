from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        phone_cat = Category(name='Phone', description='Cellphone')
        phone_cat.save()
        headphones_cat = Category(name='Headphones', description='Wireless')
        headphones_cat.save()
        monitor_cat = Category(name='Monitor', description='High resolution')
        monitor_cat.save()

        product_list = [
            {'name': 'LG', 'description': '234SDF', 'purchase_price': 1000, 'category': monitor_cat},
            {'name': 'SAMSUNG', 'description': 'JKHSSF*', 'purchase_price': 2000, 'category': monitor_cat},
            {'name': 'Apple iPhone 8', 'description': '2 CAMERAS Touch screen', 'purchase_price': 1000, 'category':phone_cat},
            {'name': 'Sony WH1000', 'description': 'wireless', 'purchase_price': 500, 'category':headphones_cat},
            {'name': 'Hyper X', 'description': 'Bluetooth 5.1', 'purchase_price': 700, 'category':headphones_cat},
        ]

        products_to_create = []
        for product_item in product_list:
            products_to_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_to_create)