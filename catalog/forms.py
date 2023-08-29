from django import forms

from catalog.models import Product, ProductVersion

CENSORED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


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


class ProductVersionForm(forms.ModelForm):

    class Meta:
        model = ProductVersion
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.instance.pk is None or self.instance.is_active is True:
                field.widget.attrs['class'] = 'form-control'

            # Отображение неактивных версий в формате только для чтения
            else:
                field.widget.attrs['class'] = 'form-control-plaintext fw-lighter'
                field.widget.attrs['readonly'] = True
