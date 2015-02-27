from django.contrib import admin
from .models import Customer, Transaction

admin.site.register(Customer)


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ("giver", "receiver", "qtty", "transaction_time", "comment")
    list_filter = ("transaction_time", "giver", "receiver")

admin.site.register(Transaction, TransactionAdmin)
