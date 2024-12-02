from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from app.models import UserInfo
from app.serializers import UserInfoSerializer


# Create your views here.

def user_list(request):
    """
    get方法请求: 获取用户列表
    post方法请求: 添加用户信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        #获取用户列表并返回
        user = UserInfo.objects.all()
        user_serializer = UserInfoSerializer(user, many=True)
        result ={
            "data": user_serializer.data,
            "code": 200,
            "msg": "success",
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        #添加用户信息
        params = JSONParser().parse(request)
        #创建序列化器
        serializer = UserInfoSerializer(data=params)
        #检查序列化器
        if serializer.is_valid():
            #检查通过,提交数据
            serializer.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return JsonResponse({"code":201,"data":serializer.data,"message":"ok"}, status=201)
        else:
            #检查失败,提示失败信息
            return JsonResponse(serializer.errors, status=400)
    #请求方法不对,返回方法问题
    return JsonResponse({"code":400,"message":f"当前地址不支持此请求方法: {request.method}"}, status=201)

def user_detail(request,id):
    """
    get方法请求: 获取用户信息
    delete方法请求: 删除用户信息
    put: 修改用户信息
    :param request:
    :return:
    """
    try:
        # 获取url传参数id
        user = UserInfo.objects.get(id=id)
    except UserInfo.DoesNotExist:
        return JsonResponse({"code":404,"message":f"未发现: {id}"}, status=404)
    if request.method == 'GET':
        user_serializer = UserInfoSerializer(user)
        result ={
            "data": user_serializer.data,
            "code": 200,
            "msg": "success",
        }
        return JsonResponse(result)
    elif request.method == 'DELETE':
        #删除资源
        user.delete()
        # 删除资源返回空对象,状态为204
        return JsonResponse({},status=204)
    elif request.method == 'PUT':
        #修改资源
        params = JSONParser().parse(request)
        serializer = UserInfoSerializer(instance=user, data=params)
        if serializer.is_valid():
            serializer.save()
            # 后端序列化器,将id设置为只读,即反序列化时,不会将id字段写入到数据库,而是让它自动生成
            return JsonResponse({"code":201,"data":serializer.data,"message":"ok"}, status=201)
        else:
            return JsonResponse({"code":400,"message":serializer.errors}, status=400)

    else:
        #请求方法不对,返回方法问题
        return JsonResponse({"code":400,"message":f"当前地址不支持此请求方法: {request.method}"}, status=201)