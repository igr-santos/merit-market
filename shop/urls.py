from django.conf.urls import patterns, url

from .views import ProductListView, ProductCreateView


urlpatterns = patterns(
    '',
    url(r'^$', ProductListView.as_view(), name="product_list"),
    url(r'^create/$', ProductCreateView.as_view(), name="product_create"),
)
