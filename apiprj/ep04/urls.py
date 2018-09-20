from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

# router 해당 뷰 셋이 제공하는 메소드/함수들에 한해 url매핑 수행.
router = DefaultRouter()
router.register(r'post',views.PostViewSet) # 2개의 url을 처리하는 뷰 함수를 만들어 등록
# /post/ urlreverse post-list
# /post/10/ urlreverse post-detail


print(router.urls)

urlpatterns = [
    url(r'',include(router.urls)),
    # url(r'^post/$',views.post_list),
    # url(r'^post/(?P<pk>\d+)/$',views.post_detail),
]