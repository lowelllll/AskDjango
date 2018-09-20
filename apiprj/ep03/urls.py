from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'post',views.PostViewSet) # post viewset 추가
router.register(r'user',views.UserViewSet) # user viewset 추가

urlpatterns = [
    # url(r'^post/$',views.PostListUseMixinView.as_view()),
    # url(r'^post/(?P<pk>\d+)/$',views.PostDetailUseMixinView.as_view()),
    url('',include(router.urls)),
    # url(r'^user/$', views.user_list),
    # url(r'^user/(?P<pk>\d+)/$', views.user_detail),
]