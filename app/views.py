from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import UserInfo
from app.serializers import UserInfoSerializer


class UserApiView(APIView):
    def get(self, request):
        #获取用户列表并返回
        user = UserInfo.objects.all()
        user_serializer = UserInfoSerializer(user, many=True)
        result ={
            "data": user_serializer.data,
            "code": 200,
            "msg": "success",
        }
        return Response(result,status=status.HTTP_200_OK)
    def post(self, request):
        #创建序列化器
        serializer = UserInfoSerializer(data=request.data)
        #检查序列化器
        if serializer.is_valid():
            #检查通过,提交数据
            serializer.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":serializer.data,"message":"ok"}, status=status.HTTP_201_CREATED)
        else:
            #检查失败,提示失败信息
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserDetailApiView(APIView):

    def get_object(self,id):
        try:
            # 获取url传参数id
            user = UserInfo.objects.get(id=id)
            return user
        except UserInfo.DoesNotExist:
            # 抛出异常
            raise Http404

    def get(self,request,id,format=None):
        user = self.get_object(id=id)
        user_serializer = UserInfoSerializer(instance=user)
        result ={
        "data": user_serializer.data,
        "code": 200,
        "msg": "success",
        }
        return Response(result)

    def put(self, request, id):
        user = self.get_object(id=id)

        serializer = UserInfoSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return Response({"code":201,"data":serializer.data,"message":"ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"code":400,"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        #删除资源
        self.get_object(id=id).delete()
        # 删除资源返回空对象,状态为204
        return Response({},status=status.HTTP_204_NO_CONTENT)
