from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from catalog.forms import ProductForm, ModeratorProductForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# Create your views here.

def contacts_view(request):
    if request.method == 'POST':
        name = request.Post.get('name')
        email = request.Post.get('email')
        message = request.Post.get('message')
        print(f'{name} ({email}): {message}')

    context = {'title': 'Контакты'}
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['version'] = kwargs['object'].version.get()
        except Version.DoesNotExist:
            context['version'] = None
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:catalog_index')
    login_url = reverse_lazy('catalog:catalog_access_denied')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_formset = inlineformset_factory(Product, Version, form=ProductForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = product_formset(self.request.POST)
        else:
            context_data['formset'] = product_formset()
        return context_data


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_index')

    def get_form_class(self):
        if self.request.user.groups.filter(name='Модератор').exists():
            return ModeratorProductForm
        else:
            return ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if (self.object.user == self.request.user or self.request.user.groups.filter(
            name='Модератор').exists() or self.request.user.is_superuser):
            return self.object
        raise Http404

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_formset = inlineformset_factory(Product, Version, form=ProductForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = product_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = product_formset(instance=self.object)
        if self.request.user.groups.filter(name='Модератор').exists():
            context_data['formset'] = ''
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class AccessDeniedView(TemplateView):
    template_name = "catalog/form_redirect.html"
