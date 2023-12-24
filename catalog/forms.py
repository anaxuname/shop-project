from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(forms.ModelForm):
    excluded_text = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        data = self.cleaned_data["name"]
        if data in self.excluded_text:
            raise ValidationError("Это наименование не допустимо!")

        return data
    def clean_description(self):
        data = self.cleaned_data["description"]
        if data in self.excluded_text:
            raise ValidationError("Это наименование не допустимо!")

        return data
    class Meta:
        model = Product
        fields = '__all__'

