from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name', 'stok', 'price', 'description', 'picture'
        )

    def clean_picture(self):
        image = self.cleaned_data.get('picture')
        if image:
            if image._size > 1024*1024:
                raise forms.ValidationError(_("Image file too large ( > 1mb )"))
            return image
        else:
            raise forms.ValidationError(_("Couldn't read uploaded image"))
