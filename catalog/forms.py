from django import forms

from catalog.models import Product, ProductVersion

CENSORED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                continue
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'image')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in CENSORED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Название не должно содержать запрещенные слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in CENSORED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Описание не должно содержать запрещенные слова')

        return cleaned_data


class ProductVersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = ProductVersion
        fields = '__all__'
