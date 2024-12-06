
from django.urls import path, include, re_path

from app import views
from app.views import UserModelViewSet, AddrModelViewSet, ImageView

#导入路由库
from rest_framework import routers

#创建简单路由
# trailing_slash=False 表示同时支持带斜杠和不带斜杠的URL
# router = routers.SimpleRouter(trailing_slash=False)
router = routers.SimpleRouter()
router.register(r'users', UserModelViewSet)
router.register(r'addrs', AddrModelViewSet)
router.register(r'uploads', ImageView)

urlpatterns = [
    # re_path(r'^users/?$', UserViewSet.as_view({"get":"list","post":"create"}), name='user'),
    # re_path(r'^users/(?P<id>\d+)/?$', UserViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"}), name='user'),
    # re_path(r'^users/?$', UserModelViewSet.as_view({"get":"list","post":"create"}), name='user'),
    # re_path(r'^users/(?P<id>\d+)/?$', UserModelViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"}), name='user'),
    # 列表url
    # re_path(r'^users/?$', UserGenericApiViewMultiples.as_view()),
    # re_path(r'^users/(?P<id>\d+)/?$', UserGenericDetailApiViewMultiples.as_view()),
    # re_path(r'^images/(?P<name>.*)/?$',views.get_image, name='image' ),
]

#拼接路由
urlpatterns += router.urls

print(router.urls)