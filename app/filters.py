#导入filters过滤器
from django_filters import rest_framework as filters
from app.models import UserInfo,Addr

class UserInfoFilter(filters.FilterSet):
    """自定义过滤器类"""
    #针对age字段进行范围查询
    min_age = filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = filters.NumberFilter(field_name='age', lookup_expr='lte')
    # 声明元信息
    class Meta:
        # 指定模型类
        model = UserInfo
        # 指定过滤字段
        fields = ['name','email','age']