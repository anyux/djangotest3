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


class AddrFilter(filters.FilterSet):
    """自定义过滤器类"""
    # 配置使用关联模型类的字段查询(关联字段__属性)
    # user__name user是Addr表的关联字段名称 __ 表示连接 name表示另一张表的关联信息
    # lookup_expr='icontains' 表示忽略大小写的模糊匹配
    name = filters.CharFilter(field_name='user__name')#, lookup_expr='icontains')
    class Meta:
        model = Addr
        fields = ['city','user']