from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE'),
        'USER': config('USER_BASE'),
        'PASSWORD': config('PASSWORD_BASE'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
    }
}