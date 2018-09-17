# accounts/urls.py

from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


urlpatterns = [
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^login/$',views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
]