from django.test import TestCase

from faker import Faker
# Create your tests here.
import json
import random

from app.models import UserInfo

# 初始化 Faker
fake = Faker('zh_CN')  # 使用中文语言环境

# 定义生成数据的函数
def generate_fake_data(num_entries):
    fake_data = []
    for _ in range(num_entries):
        data = {
            "name": fake.name(),  # 生成随机姓名
            "pwd": fake.password(length=4, special_chars=False),  # 生成随机4位数字密码
            "email": fake.email(),  # 生成随机邮箱
            "age": random.randint(20, 60)  # 生成20到60之间的随机年龄
        }
        UserInfo.objects.create(**data)
        fake_data.append(UserInfo(data))
    return fake_data

# 生成10条假数据
num_entries = 50
def post_user():
    data_list = generate_fake_data(num_entries)


# UserInfo.objects.bulk_create(data_list)