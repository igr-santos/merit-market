from django.contrib import admin
from .models import Customer, Transaction

admin.site.register(Customer)


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction

admin.site.register(Transaction, TransactionAdmin)
