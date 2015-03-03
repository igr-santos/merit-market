from datetime import timedelta
from datetime import datetime
from django.db import models
from django.conf import settings


def week_range(date=None):
    """
    Gently get from
    https://bradmontgomery.net/blog/2013/03/07/calculate-week-range-date/
    """
    if not date:
        date = datetime.now()

    year, week, dow = date.isocalendar()
    if dow == 7:
        start_date = date
    else:
        start_date = date - timedelta(dow)
    end_date = start_date + timedelta(6)
    return (start_date, end_date)


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

    def __unicode__(self):
        if self.user.get_full_name():
            name = self.user.get_full_name()
        else:
            name = self.user.username
        return name


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
