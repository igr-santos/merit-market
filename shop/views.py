from django.views.generic.list import ListView

from .models import Product

class ProductListView(ListView):
    context_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(
            stok__gt=0
        )
