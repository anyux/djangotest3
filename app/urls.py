
from django.urls import path, include, re_path

from app.views import UserApiView, UserDetailApiView, AddrApiView, AddrDetailApiView, UserGenericApiView, UserDetailGenericApiView, \
    UserGenericApiViewMixin, UserGenericDetailApiViewMixin, UserGenericApiViewMultiples, UserGenericDetailApiViewMultiples, \
    UserViewSet

urlpatterns = [
    re_path(r'^users/?$', UserViewSet.as_view({"get":"list","post":"create"}), name='user'),
    re_path(r'^users/(?P<id>\d+)/?$', UserViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"}), name='user'),
    # 列表url
    # re_path(r'^users/?$', UserGenericApiViewMultiples.as_view()),
    # re_path(r'^users/(?P<id>\d+)/?$', UserGenericDetailApiViewMultiples.as_view()),

    re_path(r'^addrs/?$', AddrApiView.as_view()),
    re_path(r'^addrs/(?P<id>\d+)/?$', AddrDetailApiView.as_view()),
]

