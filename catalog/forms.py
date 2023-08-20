from django import forms

from catalog.models import Product

censored_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for word in censored_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Название не должно содержать запрещенные слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for word in censored_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Описание не должно содержать запрещенные слова')

        return cleaned_data
