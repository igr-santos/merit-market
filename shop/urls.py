from django.conf.urls import patterns, url

from .views import ProductListView


urlpatterns = patterns(
    '',
    url(r'^$', ProductListView.as_view(), name="product_list"),
)
