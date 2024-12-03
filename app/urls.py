
from django.urls import path, include, re_path

from app.views import UserApiView, UserDetailApiView, AddrApiView, AddrDetailApiView, UserGenericApiView, UserDetailGenericApiView

urlpatterns = [
    # 列表url
    re_path(r'^users/?$', UserGenericApiView.as_view()),
    re_path(r'^users/(?P<id>\d+)/?$', UserDetailGenericApiView.as_view()),

    re_path(r'^addrs/?$', AddrApiView.as_view()),
    re_path(r'^addrs/(?P<id>\d+)/?$', AddrDetailApiView.as_view()),
]

