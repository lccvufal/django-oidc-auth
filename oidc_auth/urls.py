from django.urls import path

from . import views

urlpatterns = [
    path(r'^login/$', views.login_begin, name='oidc-login'),
    path(r'^complete/$', views.login_complete, name='oidc-complete'),
]
