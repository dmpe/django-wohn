"""
    Django settings for vanoce project.

    Generated by 'django-admin startproject' using Django 2.1.

    For more information on this file, see
    https://docs.djangoproject.com/en/2.1/topics/settings/

    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/2.1/ref/settings/
    https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
    https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
    https://docs.djangoproject.com/en/2.1/topics/i18n/
    https://docs.djangoproject.com/en/2.1/howto/static-files/
"""
import os
import sys

SECRET_KEY = 'ldj(^$nibo($d939^(mc5k)#^!b6^4yr80_4iv-7_wtm5gvzwz'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# the curpit: on local pc must be local database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'mydb',                     
        'USER': 'jm',                      
        'PASSWORD': '123',                 
        'HOST': 'localhost',               
        'PORT': '',                      
    }
}