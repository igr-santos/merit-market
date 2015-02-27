import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .exceptions import BuyError


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
        upload_to=os.path.join(settings.MEDIA_ROOT, 'shop/')
    )
    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True
    )

    def __str__(self):
        return '{} - {}'.format(self.name, self.stok)

    def buy(self, customer, qtty=1):
        """
        Check stok, price and save product
        """
        if (self.stok - qtty) < 0:
            raise BuyError('Nao possui estoque para essa compra')

        price_total = qtty * price
        if (customer.hearts < price_total):
            raise BuyError(
                'Voce nao possui coracoes suficiente para comprar esse item'
            )

        self.stok -= qtty
        self.save()
        customer.hearts -= price_total
        customer.save()

        # cria um log de compra
        BuyLog.objects.create(
            purchased_for=customer,
            product=self,
            qtty=qtty,
            price_total=price_total
        )


class BuyLog(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    purchased_for = models.ForeignKey('core.Customer')
    product = models.ForeignKey(Product)
    qtty = models.PositiveIntegerField()
    price_total = models.PositiveIntegerField()

