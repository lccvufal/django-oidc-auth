from django.conf.urls import url, include
from django.contrib import admin

import oidc_auth
import views
from oidc_auth import urls

admin.autodiscover()


urlpatterns = [
    url(r'^$', views.index),
    url(r'^oidc/', include(oidc_auth.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

