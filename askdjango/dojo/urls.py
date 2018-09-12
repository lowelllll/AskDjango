# dojo/urls.py

from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^new/$',views.post_new),
    url(r'^(?P<id>\d+)/edit/$',views.post_edit),
    url(r'^(?P<id>\d+)/$',views.post_detail),
    url(r'^sum/(?P<numbers>[\d/]+)/$',views.mysum), # sum/1/2/3/4/5.../10 여러개 변수 등록
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/',views.hello),

    url(r'^post_list1/$',views.post_list1),
    url(r'^post_list2/$',views.post_list2),
    url(r'^excel/$',views.excel_download),

    url(r'^cbv/post_list1/$',views_cbv.post_list1),
    url(r'^cbv/post_list2/$',views_cbv.post_list2),
    url(r'^cbv/post_list3/$', views_cbv.post_list3),
    url(r'^cbv/excel/$',views_cbv.excel_download),

    url(r'^post_list/$',views_cbv.post_list,name='post_list'),
    url(r'^post_detail/(?P<pk>\d+)/$',views_cbv.post_detail,name="post_detail"),
    url(r'^post_new/$',views_cbv.post_create,name="post_create"),
    url(r'^post_edit/(?P<pk>\d+)/$',views_cbv.post_edit,name="post_edit"),
    url(r'^post_delete/(?P<pk>\d+)/$',views_cbv.post_delete,name="post_delete"),
]