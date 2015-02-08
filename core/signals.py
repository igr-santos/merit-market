from django.conf import settings
from django.db.models.signals import post_save

from .models import Customer


def post_save_receiver(signal, sender, instance, **kwargs):
    """
    Create an account for every user that is register
    """
    if kwargs.get('created'):
        customer = Customer()
        customer.user = instance
        customer.save()

post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
