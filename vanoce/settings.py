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
import django_heroku

SOCIAL_AUTH_USER_MODEL = 'userMng.myUser'
AUTH_USER_MODEL = 'userMng.myUser'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ldj(^$nibo($d939^(mc5k)#^!b6^4yr80_4iv-7_wtm5gvzwz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

INSTALLED_APPS = [
    'core',
    'userMng',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'storages',
    'phonenumber_field',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)

ROOT_URLCONF = 'vanoce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 
                'core/pages/',
                'core/pages/footer', 
                'userMng/pages/',
                'userMng/pages/signup_login',
                'userMng/pages/administrace'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'vanoce.wsgi.application'

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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_EMULATED_MODE = True
AZURE_ACCOUNT_NAME = "djangowohnreal1"
AZURE_ACCOUNT_KEY = os.environ.get("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = "images"
MEDIA_URL = 'https://djangowohnreal1.blob.core.windows.net/%s/' % AZURE_CONTAINER

# Static files (CSS, JavaScript, Images)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static/css/'),
    os.path.join(PROJECT_ROOT, 'static/js/'),
]

PHONENUMBER_DB_FORMAT = 'E164'

LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_TWITTER_KEY = '3GgSqabrcz91jhPCWDcIGx5CI'
SOCIAL_AUTH_TWITTER_SECRET = 'd0rfKBTiLPdGneeNi5YEDOmICnWDZTfiqThnvP5Ltn2v7439bR'
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '806673580943-ldk1i712dfdreakds26oeq4ih1fkm54k.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'HJTheMYzP8ugMIO2ibQxiFhx'
SOCIAL_AUTH_FACEBOOK_KEY = '525287897910870'
SOCIAL_AUTH_FACEBOOK_SECRET = '469163542f06ae4ccf8fb96fc5e9585f'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['name', 'email', 'profile_picture']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '3.1'

SOCIAL_AUTH_LOGIN_URL = '/administrace/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/administrace/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/administrace/user_profile' # keep it dry
SOCIAL_AUTH_LOGIN_ERROR_URL = '404'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['user_id', 'user_created', 'user_name', 'user_first_name', 'user_last_name', 'user_email', 'user_int_tel']

SITE_ID = 1

# the curpit: on local pc must be commented out, while on heroku must be enabled
django_heroku.settings(locals())

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql', 
#        'NAME': 'mydb',                     
#        'USER': 'jm',                      
#        'PASSWORD': '123',                 
#        'HOST': 'localhost',               
#        'PORT': '',                      
#    }
#}