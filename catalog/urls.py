"""
URL configuration for shop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import contacts_view, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    AccessDeniedView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_index'),
    path('contacts/', contacts_view, name='catalog_contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='catalog_product'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('denied/', AccessDeniedView.as_view(), name='catalog_access_denied'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)