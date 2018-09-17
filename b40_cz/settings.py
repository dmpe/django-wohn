"""
Django settings for b40_cz project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import os
import sys
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "tw%5la58-@v)3_!=pur*%mh+qo1)zhw=ou7jgsy*b*gi)sjl$p"

PHONENUMBER_DB_FORMAT = 'E164'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'b40_cz.urls'

WSGI_APPLICATION = 'b40_cz.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# Change 'default' database configuration with $DATABASE_URL.
DATABASES = {}
DATABASES['default'] = os.environ.get('DATABASE_URL')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # core of user auth
    'django.contrib.contenttypes', # associate perms with models
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    
    'user_management.apps.UserManagementConfig',
    'core.apps.CoreConfig',

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 
                'core/pages/',
                'core/pages/footer', 
                'user_management/pages/',
                'user_management/pages/signup_login',
                'user_management/pages/administrace'
                ],
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
AZURE_EMULATED_MODE = True
AZURE_ACCOUNT_NAME = "djangowohnreal1"
AZURE_ACCOUNT_KEY = os.environ.get("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = "images"

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

MEDIA_URL = 'https://djangowohnreal1.blob.core.windows.net/%s/' % AZURE_CONTAINER

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
    os.path.join(PROJECT_ROOT, 'static/css/'),
    os.path.join(PROJECT_ROOT, 'static/js/'),
]

# Activate Django-Heroku.
django_heroku.settings(locals())

# Change password hashers to use Argon2 for stronger password protection
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
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


SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_TWITTER_KEY = 'foobar'
SOCIAL_AUTH_TWITTER_SECRET = 'bazqux'
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '806673580943-ldk1i712dfdreakds26oeq4ih1fkm54k.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'HJTheMYzP8ugMIO2ibQxiFhx'
SOCIAL_AUTH_FACEBOOK_KEY = '525287897910870'
SOCIAL_AUTH_FACEBOOK_SECRET = '469163542f06ae4ccf8fb96fc5e9585f'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['default', 'email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '3.1'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/administrace/index'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/administrace/user_profile' # keep it dry
SOCIAL_AUTH_LOGIN_ERROR_URL = '404'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['user_id', 'user_created', 'user_name', 'user_first_name', 'user_last_name', 'user_email', 'user_int_tel']

# SECURITY
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

AUTH_USER_MODEL = 'user_management.MyUser'
SOCIAL_AUTH_USER_MODEL = 'user_management.MyUser'
