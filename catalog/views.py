from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index_view(request):
    return render(request, 'catalog/index.html')


def contacts_view(request):
    return render(request, 'catalog/contacts.html')


def products_view(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Товары'
    }
    return render(request,'catalog/products.html', context)
