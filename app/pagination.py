'''自定义分页器类'''

from rest_framework.pagination import PageNumberPagination

class UserInfoPagination(PageNumberPagination):
    """自定义UserInfo分页器"""
    # 指定每页条数
    page_size = 10
    # 指定每页数据量的查询参数
    page_size_query_param = 'page_size'
    # 指定页码的查询参数
    page_query_param = 'page'
    # 指定每页最大数据量
    max_page_size = 20