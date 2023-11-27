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


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
        'title': 'Товар'
    }
    return render(request,'catalog/product.html', context)