from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialListView(ListView):
    model = Material


class MaterialDetailView(DetailView):
    model = Material


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')
