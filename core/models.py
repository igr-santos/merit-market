from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True
    )

    hearts = models.PositiveIntegerField(
        default=0
    )

    weekly_hearts = models.PositiveSmallIntegerField(
        default=15
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return '{}'.format(self.user.username)


class Transaction(models.Model):

    receiver = models.ForeignKey(
        Customer,
        related_name='received'
    )

    giver = models.ForeignKey(
        Customer,
        related_name='given'
    )

    qtty = models.PositiveSmallIntegerField(
        default=1
    )

    transaction_time = models.DateTimeField(
        auto_now_add=True
    )

    comment = models.CharField(
        max_length=140,
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def save(self, *args, **kwargs):
        """
        Override django's obj.save() and adds validations.

        TODO: should use forms instead.

        Validates if the gift is for yourself, and if the amount donated is
        greater than the stock of hearts.
        """
        if self.receiver == self.giver:
            raise ValueError('Receiver must be different from giver')
        elif self.giver.weekly_hearts < self.qtty:
            raise ValueError('Please select an amount smaller than your \
                 available hearts')

        self.giver.weekly_hearts -= self.qtty
        self.giver.save()
        self.receiver.hearts += self.qtty
        self.receiver.save()

        return super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} to {1} - {2} hearts".format(
               self.giver,
               self.receiver,
               self.qtty)
