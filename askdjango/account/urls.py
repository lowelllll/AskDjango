# account/urls.py

from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


urlpatterns = [
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^login/$',auth_views.login,name='login',kwargs={
        'template_name':'account/login_form.html',
        'authentication_form':LoginForm
    }),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$',views.signup,name='signup'),
]