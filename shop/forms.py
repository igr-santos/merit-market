# coding: utf-8

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Product

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product

	 def clean_picture(self):
         image = self.cleaned_data.get('picture',False)
         if image:
             if image._size > 2*1024*1024:
                   raise ValidationError(_("Image file too large ( > 2mb )"))
             return image
         else:
             raise ValidationError(_("Couldn't read uploaded image"))