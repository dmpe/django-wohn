"""
    Django settings for melive project.

    For more information on this file, see
    https://docs.djangoproject.com/en/2.2/topics/settings/
"""
import logging
import os
import socket

import debug_toolbar
from azure.core.exceptions import AzureError

# for Azure Key Vault
from azure.identity import ChainedTokenCredential, ClientSecretCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
from django.contrib.messages import constants as message_constants
from sendgrid import SendGridAPIClient

from myAzure.az_connect import AzureConnection
from myAzure.az_storage import *

azCon = AzureConnection()
azCon.main()
client = SecretClient(vault_url="https://b40.vault.azure.net/", credential=azCon.credentials)

AUTH_USER_MODEL = "core.myUser"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


def custom_show_toolbar(request):
    return True


ALLOWED_HOSTS = ["*"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

if azCon.env == "development":
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": custom_show_toolbar}
    INTERNAL_IPS = ["127.0.0.1", os.environ["DOCKER_HOST"]]
else:
    INTERNAL_IPS = ["127.0.0.1"]
    # DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": custom_show_toolbar}


INSTALLED_APPS = [
    "django_extensions",
    "core",
    "userMng",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "storages",
    "phonenumber_field",
    "widget_tweaks",
    "timezone_field",
    "django_countries",
    "graphene_django",
    "debug_toolbar",
    "graphiql_debug_toolbar",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "graphiql_debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTHENTICATION_BACKENDS = (
    # for username and (!) email authentication
    "core.backends.EmailUserNameAuthBackend",
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
)


hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

# Where your Graphene schema lives
GRAPHENE = {"SCHEMA": "melive.schema.schema", "MIDDLEWARE": ["graphql_jwt.middleware.JSONWebTokenMiddleware"]}

ROOT_URLCONF = "melive.urls"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            "core/pages/",
            "core/pages/emails",
            "core/pages/footer",
            "core/pages/signup_login",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages"
            ],
            "debug": DEBUG,
        },
    }
]

WSGI_APPLICATION = "melive.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

MESSAGE_TAGS = {
    message_constants.INFO: "info",
    message_constants.SUCCESS: "success",
    message_constants.WARNING: "warning",
    message_constants.ERROR: "danger",
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Prague"
USE_I18N = True
USE_L10N = True
USE_TZ = True

COUNTRIES_FIRST = ["CZ", "SK"]
COUNTRIES_FIRST_REPEAT = True
COUNTRIES_FIRST_BREAK = "---------------"

DEFAULT_FILE_STORAGE = "myAzure.az_storage.AzureMediaStorage"
STATICFILES_STORAGE = "myAzure.az_storage.AzureStaticStorage"

MEDIA_LOCATION = "user-profile-photos"
MEDIA_URL = "https://melivexyz5555.blob.core.windows.net/%s/" % MEDIA_LOCATION

STATIC_URL = "https://melivexyz5555.blob.core.windows.net/"

AZURE_EMULATED_MODE = False
AZURE_OVERWRITE_FILES = True

PHONENUMBER_DB_FORMAT = "E164"

# where is login page
LOGIN_URL = "core:login"
LOGIN_REDIRECT_URL = "userMng:userMng_index"

LOGOUT_REDIRECT_URL = "core:homepage"

SITE_ID = 1

EMAIL_HOST = "smtp.sendgrid.net"
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
EMAIL_HOST_USER = "azure_a880e6655cecd4d33d0a10c5f893868f@azure.com"
EMAIL_HOST_PASSWORD = client.get_secret("EMAIL-HOST-PASSWORD").value
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SENDGRID_API_KEY = SendGridAPIClient(client.get_secret("SENDGRID-API-KEY").value)

MY_EMAIL = client.get_secret("MY-EMAIL").value

# used when pushing via git
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
