from django.db.models import Sum
from .models import Customer, week_range


def top_givers(request):
    date_range = week_range()
    return {
        'top_givers': Customer.objects.filter(
            given__transaction_time__range=date_range).annotate(
            Sum('given__qtty')).order_by('-given__qtty__sum')[:5]
    }


def top_receivers(request):
    date_range = week_range()
    return {
        'top_receivers': Customer.objects.filter(
            received__transaction_time__range=date_range).annotate(
            Sum('received__qtty')).order_by('-received__qtty__sum')[:5]
    }


def top_users(request):
    data = {}
    data.update(top_givers(request))
    data.update(top_receivers(request))
    return data
