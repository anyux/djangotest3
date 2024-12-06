#认证库
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, throttle_classes
#权限权限
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
#导入drf过滤器
from rest_framework import filters, status

from app.filters import UserInfoFilter, AddrFilter
from app.models import UserInfo, Addr, ImageModel
from app.pagination import UserInfoPagination
from app.serializers import UserInfoSerializer, AddrSerializer, ImageSerializer


class UserModelViewSet(ModelViewSet):
    # throttle_classes = (UserRateThrottle,)
    #指定认证的方式
    # authentication_classes = (BasicAuthentication, SessionAuthentication,TokenAuthentication)
    # 设置访问权限认证
    # permission_classes = (IsAuthenticated,)
    # 导入查询结果集
    queryset = UserInfo.objects.all()
    # 导入序列化类
    serializer_class = UserInfoSerializer
    # 设置查询字段
    lookup_field='id'
    # 方式1: 过滤字段
    # filterset_fields = ('name','email')
    # 方式2: 指定过滤器类
    filterset_class = UserInfoFilter

    # 指定排序的过滤器
    filter_backends = (filters.OrderingFilter,)
    # 指定排序的字段
    ordering_fields = ('age','id',)

    # # 默认每页数据量
    # page_size = 20
    # # 前端发送的每页数目关键字名
    # page_size_query_param = 'page_size'
    # #每页的数据量的最大值
    # max_page_size = 30

    #指定分页器类
    pagination_class = UserInfoPagination

    #定义list方法
    # def list(self, request, *args, **kwargs):
    #     print(a)
    #     return super().list(request, *args, **kwargs)

class AddrModelViewSet(ModelViewSet):
    #指定认证的方式
    # authentication_classes = (BasicAuthentication, SessionAuthentication,TokenAuthentication)
    # 设置访问权限认证
    # permission_classes = (IsAuthenticated,)
    # 导入查询结果集
    queryset = Addr.objects.all()
    # 导入序列化类
    serializer_class = AddrSerializer
    # 设置查询字段
    lookup_field='id'

    # 方式1: 过滤字段
    # filterset_fields = ('name','email')
    # 方式2: 指定过滤器类
    filterset_class = AddrFilter


from rest_framework.viewsets import mixins,GenericViewSet
class ImageView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):

    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        """自定义图片上传功能"""
        image = request.data.get('path')
        # 获取图片名称
        name = image.name
        # 获取图片大小
        size = image.size
        # 获取图片类型
        type = image.content_type

        # 设置图片上传大小能起过30k
        if size > 1024 * 30000:
            max_size = {
                'error': "图片大小不能超过30k"
            }
            return Response(max_size, status=status.HTTP_400_BAD_REQUEST)
        elif type not in ['image/png', 'image/jpeg', 'image/jpg', 'image/gif', 'image/bmp']:
            type_error = {
                'error': f"图片类型不正确{type}"
            }
            return Response(type_error, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().create(request, *args, **kwargs)

