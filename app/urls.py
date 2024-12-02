
from django.urls import path, include, re_path

from app.views import UserApiView, UserDetailApiView

urlpatterns = [
    # 列表url
    re_path(r'^users/?$', UserApiView.as_view()),
    re_path(r'^users/(?P<id>\d+)/?$', UserDetailApiView.as_view()),

]

