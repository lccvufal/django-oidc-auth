from django.urls import path, include
from django.contrib import admin

import oidc_auth
from . import views
from .oidc_auth import urls

admin.autodiscover()


urlpatterns = [
    path(r'^$', views.index),
    path(r'^oidc/', include(oidc_auth.urls)),
    path(r'^admin/', include(admin.site.urls)),
]

