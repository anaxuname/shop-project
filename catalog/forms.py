from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
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
