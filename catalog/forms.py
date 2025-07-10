from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = {
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
}

def contains_forbidden_word(value):
    words_in_value = set(value.lower().split())
    if words_in_value & FORBIDDEN_WORDS:
        raise forms.ValidationError("Поле содержит запрещённое слово.")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            return name
        contains_forbidden_word(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description') or ''
        contains_forbidden_word(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError("Цена должна быть больше нуля.")
        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label != "Описание":
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control', 'rows': 4})
        # if 'is_published' in self.fields:
        #     self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})
