from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

def my_exception_handler(exc, context):
    # 自定义的异常处理方法
    response = exception_handler(exc, context)

    # 由drf判断是否处理异常
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['message'] = response.data.get('detail','An error occurred')
    else:
        # 如果drf没处理,需要自定义处理
        data = {"error":"就异常了"}
        response = Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response