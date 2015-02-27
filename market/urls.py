from django.conf.urls import patterns, include, url
from django.contrib import admin

from core.views import TransactionCreateView


urlpatterns = patterns(
    '',
    url(r'^dashboard/$',
        TransactionCreateView.as_view(), name="dashboard"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shop/', include('shop.urls', namespace='shop')),

    url(r'^$', 'django.contrib.auth.views.login',
        kwargs={'template_name': 'core/index.html'}, name="login"),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        kwargs={'login_url': '/'}, name='logout'),
)
