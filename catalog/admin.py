from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
