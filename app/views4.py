from django.http import Http404
from rest_framework import status, mixins, viewsets
from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from app.models import UserInfo, Addr
from app.serializers import UserInfoSerializer, AddrSerializer


class UserApiView(APIView):
    # 定义模型参数
    model = UserInfo
    # 定义模型序列化参数
    serializer = UserInfoSerializer

    def get(self, request):
        #获取用户列表并返回
        data = self.model.objects.all()
        ser_data = self.serializer(data, many=True)
        result ={
            "data": ser_data.data,
            "code": 200,
            "msg": "success",
        }
        return Response(result,status=status.HTTP_200_OK)
    def post(self, request):
        #创建序列化器
        ser_data = self.serializer(data=request.data)
        #检查序列化器
        if ser_data.is_valid():
            #检查通过,提交数据
            ser_data.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":ser_data.data,"message":"ok"}, status=status.HTTP_201_CREATED)
        else:
            #检查失败,提示失败信息
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)





class UserDetailApiView(APIView):

    # 定义模型参数
    model = UserInfo
    # 定义序列化器参数
    serializer = UserInfoSerializer

    def get_object(self,id):
        try:
            # 获取url传参数id
            user = self.model.objects.get(id=id)
            return user
        except UserInfo.DoesNotExist:
            # 抛出异常
            raise Http404

    def get(self,request,id,format=None):
        user = self.get_object(id=id)
        user_serializer = self.serializer(instance=user)
        result ={
        "data": user_serializer.data,
        "code": 200,
        "msg": "success",
        }
        return Response(result)

    def put(self, request, id):
        user = self.get_object(id=id)

        ser_data = self.serializer(instance=user, data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":ser_data.data,"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"code":400,"message":ser_data.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        #删除资源
        self.get_object(id=id).delete()
        # 删除资源返回空对象,状态为204
        return Response({},status=status.HTTP_204_NO_CONTENT)


class AddrApiView(APIView):
    # 定义模型参数
    model = Addr
    # 定义模型序列化参数
    serializer = AddrSerializer

    def get(self, request):
        #获取用户列表并返回
        data = self.model.objects.all()
        ser_data = self.serializer(data, many=True)
        result ={
            "data": ser_data.data,
            "code": 200,
            "msg": "success",
        }
        return Response(result,status=status.HTTP_200_OK)
    def post(self, request):
        #创建序列化器
        ser_data = self.serializer(data=request.data)
        #检查序列化器
        if ser_data.is_valid():
            #检查通过,提交数据
            ser_data.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":ser_data.data,"message":"ok"}, status=status.HTTP_201_CREATED)
        else:
            #检查失败,提示失败信息
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)





class AddrDetailApiView(APIView):

    # 定义模型参数
    model = Addr
    # 定义序列化器参数
    serializer = AddrSerializer

    def get_object(self,id):
        try:
            # 获取url传参数id
            user = self.model.objects.get(id=id)
            return user
        except UserInfo.DoesNotExist:
            # 抛出异常
            raise Http404

    def get(self,request,id,format=None):
        user = self.get_object(id=id)
        user_serializer = self.serializer(instance=user)
        result ={
            "data": user_serializer.data,
            "code": 200,
            "msg": "success",
        }
        return Response(result)

    def put(self, request, id):
        user = self.get_object(id=id)

        ser_data = self.serializer(instance=user, data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":ser_data.data,"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"code":400,"message":ser_data.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        #删除资源
        self.get_object(id=id).delete()
        # 删除资源返回空对象,状态为204
        return Response({},status=status.HTTP_204_NO_CONTENT)

class UserGenericApiView(GenericAPIView):
    # 定义模型参数
    queryset = UserInfo.objects.all()
    # 定义序列化器参数
    serializer_class = UserInfoSerializer

    def get(self, request):
        #获取用户列表并返回
        data = self.get_queryset()
        # 使用 many=True 参数来序列化多个对象
        ser_data = self.get_serializer(data,many=True)
        result ={
            "data": ser_data.data,
            "code": 200,
            "msg": "success",
        }
        return Response(result,status=status.HTTP_200_OK)
    def post(self, request):
        #创建序列化器
        ser_data = self.get_serializer(data=request.data)
        #检查序列化器
        if ser_data.is_valid():
            #检查通过,提交数据
            ser_data.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":ser_data.data,"message":"ok"}, status=status.HTTP_201_CREATED)
        else:
            #检查失败,提示失败信息
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailGenericApiView(GenericAPIView):
    # 定义模型参数
    queryset = UserInfo.objects.all()
    # 定义序列化器参数
    serializer_class = UserInfoSerializer
    # 指定查询参数
    lookup_field='id'

    def get(self,request,id,format=None):
        user = self.get_object()
        user_serializer = self.get_serializer(instance=user)
        result ={
            "data": user_serializer.data,
            "code": 200,
            "msg": "success",
        }
        return Response(result)

    def put(self, request, id):
        user = self.get_object()

        ser_data = self.get_serializer(instance=user, data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":ser_data.data,"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"code":400,"message":ser_data.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        #删除资源
        self.get_object().delete()
        # 删除资源返回空对象,状态为204
        return Response({},status=status.HTTP_204_NO_CONTENT)

class UserGenericApiViewMixin(GenericAPIView,
                              mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              ):
    # 导入查询结果集
    queryset = UserInfo.objects.all()
    # 导入序列化类
    serializer_class = UserInfoSerializer

    def get(self, request,*args,**kwargs):
        # 复用mixins.ListModelMixin类的list方法,
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        # 复用mixins.CreateMixin类的create方法
        return self.create(request,*args,**kwargs)

class UserGenericDetailApiViewMixin(GenericAPIView,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin
                                    ):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field='id'

    def get(self,request,*args,**kwargs):
        #复用mixins.RetrieveModelMixin类的retrieve方法,获取单条数据
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        # 复用mixins.UpdateModelMixin的update方法,更新单条数据
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        # 复用mixins.DestoryModelMixin类的destory方法,删除单条数据
        return self.destroy(request,*args,**kwargs)


class UserGenericApiViewMultiples(
                              generics.ListAPIView,
                              generics.CreateAPIView
                              ):
    # 导入查询结果集
    queryset = UserInfo.objects.all()
    # 导入序列化类
    serializer_class = UserInfoSerializer

class UserGenericDetailApiViewMultiples(
                                    generics.RetrieveAPIView,
                                    generics.UpdateAPIView,
                                    generics.DestroyAPIView
                                    ):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field='id'

class UserViewSet(viewsets.ViewSet):

    def list(self,request):
        # 获取查询集
        queryset = UserInfo.objects.all()
        # 将查询集序列化
        serializer = UserInfoSerializer(queryset, many=True)
        # 返回序列化结果
        return Response(serializer.data)

    def create(self,request):
        # 将请求数据序列化
        serializer = UserInfoSerializer(data=request.data)
        # 检查序列化是否通
        if serializer.is_valid():
            # 保存数据
            serializer.save()
            # 返回数据结果
            return Response(serializer.data)
        # 返回序列化错误
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,id):
        # 获取查询集
        queryset = UserInfo.objects.all()
        # 在查询集中过滤指定id的数据
        user = get_object_or_404(queryset,id=id)
        # 将过滤结果序列化
        serializer = UserInfoSerializer(user)
        # 返回序列化结果
        return Response(serializer.data)

    def update(self,request,id):
        # 获取查询集
        queryset = UserInfo.objects.all()
        #在查询中过滤指定id的数据
        user = get_object_or_404(queryset,id=id)
        #将过滤结果序列化
        serializer = UserInfoSerializer(user, data=request.data)
        # 检查序列化是否通
        if serializer.is_valid():
            # 保存数据
            serializer.save()
            # 返回数据结果
            return Response(serializer.data)
            # 返回序列化错误
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,id):
        # 获取查询集
        queryset = UserInfo.objects.all()
        #在查询中过滤指定id的数据
        user = get_object_or_404(queryset,id=id)
        #删除数据
        user.delete()
        #返回数据结果
        return Response({})


class UserModelViewSet(ModelViewSet):
    # 导入查询结果集
    queryset = UserInfo.objects.all()
    # 导入序列化类
    serializer_class = UserInfoSerializer
    # 设置查询字段
    lookup_field='id'


class CustomUserViewSet(ReadOnlyModelViewSet,
                        mixins.CreateModelMixin,
                        ):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field='id'