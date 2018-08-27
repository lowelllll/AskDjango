from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$',views.mysum), # sum/1/2/3/4/5.../10 여러개 변수 등록
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/',views.hello),
    url(r'^post_list1/$',views.post_list1),
    url(r'^post_list2/$',views.post_list2),
    url(r'^excel/$',views.excel_download),
]