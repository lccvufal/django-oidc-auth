from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^login/$', views.login_begin, name='oidc-login'),
    re_path(r'^complete/$', views.login_complete, name='oidc-complete')
]
