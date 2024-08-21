from django.urls import re_path, include
from django.contrib import admin

import oidc_auth
from . import views
from .oidc_auth import urls

admin.autodiscover()


urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^oidc/', include(oidc_auth.urls)),
    re_path(r'^admin/', include(admin.site.urls)),
]

