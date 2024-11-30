from rest_framework import serializers



class UserInfoSerializer(serializers.Serializer):
    """定义序列化器"""
    name = serializers.CharField(max_length=20)
    id = serializers.IntegerField()
    pwd = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=40)
    age = serializers.IntegerField(min_value=0, max_value=150)
