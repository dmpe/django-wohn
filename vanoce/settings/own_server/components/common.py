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
import logging

# for bootstrap, to make message classes consistent with the framework
from django.contrib.messages import constants as message_constants

# for Azure Key Vault
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_active_directory import MSIAuthentication
from sendgrid import *

# for celery tasks - scheduling
from celery.schedules import *

credentials = MSIAuthentication(resource='https://vault.azure.net')
client = KeyVaultClient(credentials)

SOCIAL_AUTH_USER_MODEL = 'userMng.myUser'
AUTH_USER_MODEL = 'userMng.myUser'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
# https://crontab.guru/#13_13_*_1-12_1
CELERY_BEAT_SCHEDULE = {
    'parse_forex_data': {
        'task': 'userMng.tasks.parse_forex_data',
        'schedule': crontab(minute=13, hour=13, day_of_month = '*', day_of_week = 1, month_of_year = '1-12')
    }
}

INSTALLED_APPS = [
    'django_extensions',
    'core',
    'userMng',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'corsheaders',
    'storages',
    'phonenumber_field',
    'crispy_forms',
    'widget_tweaks',
    'markdownx',
    'timezone_field',
    'django_countries',
    'rest_framework',
    'pinax.templates',
    'pinax.messages',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
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
    'userMng.backends.EmailUserNameAuthBackend', # for username and (!) email authentication
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

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    #'social.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social.pipeline.disconnect.disconnect',
)


ROOT_URLCONF = 'vanoce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 
                'templates/base_splitting',
                'core/pages/',
                'core/pages/emails',
                'core/pages/footer', 
                'userMng/pages/',
                'userMng/pages/emails',
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
                'pinax.messages.context_processors.user_messages',
            ],
            'debug': DEBUG,
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

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

MESSAGE_TAGS = {
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Prague'
USE_I18N = True
USE_L10N = True
USE_TZ = True

COUNTRIES_FIRST = ["CZ", "SK"]
COUNTRIES_FIRST_REPEAT = True
COUNTRIES_FIRST_BREAK = "---------------"

# Static files (CSS, JavaScript, Images)
AZURE_ACCOUNT_NAME = "djangowohnreal1"
AZURE_ACCOUNT_KEY = client.get_secret("https://b40.vault.azure.net/", "AZURE-ACCOUNT-KEY", "2c71faab5f684de88893557e09c24fbf").value

DEFAULT_FILE_STORAGE = 'backend.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'backend.custom_azure.AzureStaticStorage'

MEDIA_LOCATION = "user-profile-photos"
MEDIA_URL = 'https://djangowohnreal1.blob.core.windows.net/%s/' % MEDIA_LOCATION

STATIC_URL = 'https://djangowohnreal1.blob.core.windows.net/'

AZURE_EMULATED_MODE = False
AZURE_OVERWRITE_FILES = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static/css/'),
    os.path.join(PROJECT_ROOT, 'static/js/'),
]

PHONENUMBER_DB_FORMAT = 'E164'

LOGIN_URL = 'login' # where is login page
LOGIN_REDIRECT_URL = 'userMng_index'

LOGOUT_REDIRECT_URL = 'homepage'

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_TWITTER_KEY = client.get_secret("https://b40.vault.azure.net/", "SOCIAL-AUTH-TWITTER-KEY", "7cf698527d95469cb91474875b29a3e0").value
SOCIAL_AUTH_TWITTER_SECRET = client.get_secret("https://b40.vault.azure.net/", "SOCIAL-AUTH-TWITTER-SECRET", "5f99c09acc8e41d58c87e18cdf8dcd11").value
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = client.get_secret("https://b40.vault.azure.net/", "SOCIAL-AUTH-GOOGLE-OAUTH2-KEY", "e37953c45b474a46b38c1ae02e5c541b").value
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = client.get_secret("https://b40.vault.azure.net/", "SOCIAL-AUTH-GOOGLE-OAUTH2-SECRET", "229ada441766486781ab00c5a63e3ebf").value
SOCIAL_AUTH_FACEBOOK_KEY = client.get_secret("https://b40.vault.azure.net/", "SOCIAL-AUTH-FACEBOOK-KEY", "e02a18956b4b46f6868ca9b9a3c5608d").value
SOCIAL_AUTH_FACEBOOK_SECRET = client.get_secret("https://b40.vault.azure.net/", "SOCIAL-AUTH-FACEBOOK-SECRET", "f439106e5d77442b8607165cf61cf260").value
SOCIAL_AUTH_FACEBOOK_API_VERSION = '3.1'

SOCIAL_AUTH_LOGIN_URL = '/administrace/' # not same as LOGIN_URL !
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/administrace/profile' # keep it dry
SOCIAL_AUTH_LOGIN_ERROR_URL = '404'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['user_id', 'user_created', 'user_name', 'user_first_name', 'user_last_name', 'user_email', 'user_int_tel', 'country']

SITE_ID = 1

EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_PORT = 465
#EMAIL_USE_SSL = True
EMAIL_HOST_USER = "azure_a880e6655cecd4d33d0a10c5f893868f@azure.com"
EMAIL_HOST_PASSWORD = client.get_secret("https://b40.vault.azure.net/", "EMAIL-HOST-PASSWORD", "08655250f5ab42a88971cc19eaedd241").value
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SENDGRID_API_KEY = SendGridAPIClient(client.get_secret("https://b40.vault.azure.net/", "SENDGRID-API-KEY", "5e84e665a6624d98982c836808220c7a").value)

GOOGLE_RECAPTCHA_V3 = client.get_secret("https://b40.vault.azure.net/", "GOOGLE-RECAPTCHA-V3", "7bd3d869a8be4835b3a3a6b27ce411b5").value

MY_EMAIL = client.get_secret("https://b40.vault.azure.net/", "MY-EMAIL", "27ba21440e1f41798df0217622c54dda").value

# used when pushing via git
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)


