from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from templated_email import send_templated_mail

from .models import Transaction
from .mixins import LoginRequiredMixin
from .forms import TransactionForm


class IndexView(TemplateView):
    template_name = 'core/index.html'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    form_class = TransactionForm
    fields = ('receiver', 'qtty', 'comment', )
    template_name = 'core/transaction.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super(TransactionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """
        Giver is logged user in request
        """
        self.object = form.save(commit=False)
        self.object.giver = self.request.user.customer
        self.object.save()

        # send email for user receives heart
        if hasattr(settings, 'FROM_EMAIL'):
            send_templated_mail(
                template_name='received_hearts',
                from_email=settings.FROM_EMAIL,
                recipient_list=[self.object.receiver.user.email, ],
                context={
                    'transaction': self.object,
                    'url_domain': self.request.build_absolute_uri()
                }
            )

        return HttpResponseRedirect(self.get_absolute_url())

    def get_absolute_url(self):
        return reverse('dashboard')

    def get_context_data(self, *args, **kwargs):
        context = super(TransactionCreateView,
                        self).get_context_data(*args, **kwargs)

        transactions_to_me = Transaction.objects.filter(
            receiver=self.request.user
        ).order_by('-transaction_time')[:15]
        context['transactions_to_me'] = transactions_to_me

        my_transactions = Transaction.objects.filter(
            giver=self.request.user
        ).order_by('-transaction_time')[:15]
        context['my_transactions'] = my_transactions

        last_transactions = Transaction.objects.all().order_by(
            '-transaction_time')[:15]
        context['last_transactions'] = last_transactions

        return context
