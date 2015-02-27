from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=180
    )
    stok = models.PositiveIntegerField(
        _('Stok')
    )
    price = models.PositiveIntegerField(
        _('Price')
    )
    description = models.TextField(
        _('Description'),
        null=True,
        blank=True
    )
    picture = models.ImageField(
        _('Picture'),
        upload_to='shop/'
    )
