from rest_framework import serializers

from app.models import UserInfo


class UserInfoSerializer(serializers.Serializer):
    """定义序列化器"""
    name = serializers.CharField(max_length=20)
    id = serializers.IntegerField(read_only=True)
    pwd = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=40)
    age = serializers.IntegerField(min_value=0, max_value=150)

class AddressSerializer(serializers.Serializer):
    """定义地址表序列化器"""
    id = serializers.IntegerField(read_only=True)
    mobile = serializers.CharField(max_length=18)
    city = serializers.CharField(max_length=10)
    info = serializers.CharField(max_length=200)
    # 返回关联模型对象的主键,此处必须指定关联到的对象queryset或者指定参数 read_only=True
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # 返回整个外键关联的信息
    # user = UserInfoSerializer()
    # 返回该模型的__str__返回值
    # user = serializers.StringRelatedField()
    # 返回自定义的关联的外键字段,只能指定一个字段
    # user = serializers.SlugRelatedField(read_only=True,slug_field='email')
