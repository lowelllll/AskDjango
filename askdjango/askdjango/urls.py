"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect

def root(request):
    return redirect('blog:post_list')

urlpatterns = [
    # url(r'^$',root), # redirect
    url(r'^$',lambda r:redirect('blog:post_list'),name='root'), # lambda로 사용

    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^dojo/',include('dojo.urls',namespace='dojo')),
    url(r'^account/',include('account.urls',namespace='account')), # 원래 auth에는 네임스페이스를 사용하지 않음!
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # DEBUG=False 일 때는 static 함수에서 빈 리스트를 리턴

if settings.DEBUG: # DEBUG 항목이 TRUE일 때
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/',include(debug_toolbar.urls)) # DEBUG 툴바 추가
    ]