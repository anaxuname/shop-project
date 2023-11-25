from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index_view(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Товары'
    }
    return render(request, 'catalog/index.html', context)


def contacts_view(request):
    if request.method == 'POST':
        name = request.Post.get('name')
        email = request.Post.get('email')
        message = request.Post.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


def products_view(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Товары2'
    }
    return render(request,'catalog/products.html', context)
