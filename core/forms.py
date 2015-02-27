# coding: utf-8
from django import forms
from .models import Transaction
from .models import Customer


class TransactionForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=Transaction.objects.none())

    def __init__(self, user, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].queryset = Customer.objects.exclude(
            user=user)

    class Meta:
        model = Transaction
        exclude = ('giver', )
