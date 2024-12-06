"""
Django settings for djangotest3 project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lws(qvnd#y*-t#mtn(3^14p9!iy8dvvv8tu30#*^9y&)z*m9a!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 添加drf
    "rest_framework",
    # 添加应用
    "app",
    #后端过滤
    "django_filters",
    #api文档
    'coreapi',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangotest3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangotest3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "test3",
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST 框架配置
#在配置文件中配置全局默认的
REST_FRAMEWORK = {
    # 默认认证类
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 基于 HTTP Basic 认证的身份验证方式,客户端需要在请求头中提供Authorization 字段,
        # 内容为 Basic <credentials>，其中 <credentials> 是 username:password 经过 Base64 编码后的字符串
        # 适用于测试场景
        # 'rest_framework.authentication.BasicAuthentication',
        # 依赖于 Django 的会话（session）框架,服务器会在用户的浏览器中设置一个会话 cookie，
        # 后续的请求会携带这个 cookie 来标识用户身份
        # 'rest_framework.authentication.SessionAuthentication',
        # 基于令牌的认证机制,用户通过登录获取一个令牌（token），后续的请求需要在请求头中提供 Authorization 字段，内容为 Token <token>
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    # 默认权限管理类
    'DEFAULT_PERMISSION_CLASSES': (
        # 表示只有登录的用户才能访问
        # 'rest_framework.permissions.IsAuthenticated',
        #如果未指明,默认采用所有用户均可访问
        # 'rest_framework.permissions.AllowAny',
        # 表示只有超级管理员才能访问
        # 'rest_framework.permissions.IsAdminUser',
        # 认证的用户可以完全操作,否则只能get读取
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    # 设置限流类型
    'DEFAULT_THROTTLE_CLASSES': (
        # 限制所有匿名未认证用户
        # 'rest_framework.throttling.AnonRateThrottle',
        # 限制认证用户
        # 'rest_framework.throttling.UserRateThrottle',
    ),
    # 设置限制的频率
    'DEFAULT_THROTTLE_RATES': {
        # 频率周期
        # second:秒,minute:分钟,hour:小时,day:每天
        # 未认证用户
        'anon': '1/day',
        # 认证用户
        'user': '10/minute',
    },
    #在配置文件中增加过滤后端的设置
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    #设置api文档配置
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    #调DRF使用的默认过滤器filter_backends = [OrderingFilter]
    'DEFAULT_FILTER_BACKENDS': (
        # 指定django_filters中的过滤器过滤
        'django_filters.rest_framework.DjangoFilterBackend',
        # 指定drf自带的排序过滤器过滤
        'rest_framework.filters.OrderingFilter',
    ),

    #设置分类器,全局配置,对所有获取数据列表的接口生效
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #指定每页数据量
    # 'PAGE_SIZE': 10,
    # 默认的异常处理方式
    # "EXCEPTION_HANDLER": "rest_framework.views.exceptions",
    # 使用自定义异常处理方式
    # "EXCEPTION_HANDLER": "app.utils.custom_exception_handler.my_exception_handler"
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

# 指定文件上传存放的路径:方式1
# MEDIA_ROOT = BASE_DIR / 'file' / 'image'
#指定文件上传存放的路径:方式2
MEDIA_ROOT = os.path.join(BASE_DIR,'file','image')
#指定文件的url路径
MEDIA_URL = '/media/'