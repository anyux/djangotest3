from django.urls import path, include, re_path

from app.views import user_list, user_detail

urlpatterns = [
    # 列表url
    re_path(r'^users/?$',user_list,name='user_list'),
    # 单个节点url
    re_path(r'^users/?(?P<id>\d+)/?$',user_detail,name='user_detail'),
]
