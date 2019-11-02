"""
    Django settings for melive project.

    For more information on this file, see
    https://docs.djangoproject.com/en/2.2/topics/settings/
"""
import logging
import os
import socket

import debug_toolbar

# for Azure Key Vault
from azure.identity import ManagedIdentityCredential, ClientSecretCredential, ChainedTokenCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError

from django.contrib.messages import constants as message_constants
from sendgrid import SendGridAPIClient

from myAzure.az_connect import AzureConnection
from myAzure.az_storage import *

azCon = AzureConnection()
azCon.main()
client = SecretClient(vault_url="https://b40.vault.azure.net/", credential=azCon.credentials)

SOCIAL_AUTH_USER_MODEL = "core.myUser"
AUTH_USER_MODEL = "core.myUser"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if azCon.env != "development":
    ALLOWED_HOSTS = ["*"]
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True
    INTERNAL_IPS = ["127.0.0.1", os.environ["DOCKER_HOST"]]
else:
    INTERNAL_IPS = ["127.0.0.1"]


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
    "social_django",
    "corsheaders",
    "storages",
    "phonenumber_field",
    "crispy_forms",
    "widget_tweaks",
    "timezone_field",
    "django_countries",
    "pinax.templates",
    "pinax.messages",
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
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTHENTICATION_BACKENDS = (
    # for Google authentication
    "social_core.backends.open_id.OpenIdAuth",
    "social_core.backends.google.GoogleOpenId",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.twitter.TwitterOAuth",
    "social_core.backends.facebook.FacebookOAuth2",
    # for username and (!) email authentication
    "core.backends.EmailUserNameAuthBackend",
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
    "social_core.pipeline.social_auth.associate_by_email",
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    # 'social.pipeline.disconnect.allowed_to_disconnect',
    # Collects the social associations to disconnect.
    "social.pipeline.disconnect.get_entries",
    # Revoke any access_token when possible.
    "social.pipeline.disconnect.revoke_tokens",
    # Removes the social associations.
    "social.pipeline.disconnect.disconnect",
)


def custom_show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": custom_show_toolbar}

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

# Where your Graphene schema lives
GRAPHENE = {
    "SCHEMA": "melive.schema.schema",
    "MIDDLEWARE": ["graphql_jwt.middleware.JSONWebTokenMiddleware"],
}

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
            "userMng/pages/",
            "userMng/pages/administrace",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
                "pinax.messages.context_processors.user_messages",
            ],
            "debug": DEBUG,
        },
    }
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

WSGI_APPLICATION = "melive.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
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

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_TWITTER_KEY = client.get_secret(
    "SOCIAL-AUTH-TWITTER-KEY"
).value
SOCIAL_AUTH_TWITTER_SECRET = client.get_secret(
    "SOCIAL-AUTH-TWITTER-SECRET"
).value
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = client.get_secret(
    "SOCIAL-AUTH-GOOGLE-OAUTH2-KEY"
).value
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = client.get_secret(
    "SOCIAL-AUTH-GOOGLE-OAUTH2-SECRET"
).value
SOCIAL_AUTH_FACEBOOK_KEY = client.get_secret(
    "SOCIAL-AUTH-FACEBOOK-KEY"
).value
SOCIAL_AUTH_FACEBOOK_SECRET = client.get_secret(
    "SOCIAL-AUTH-FACEBOOK-SECRET"
).value
SOCIAL_AUTH_FACEBOOK_API_VERSION = "4.0"

# not same as LOGIN_URL !
SOCIAL_AUTH_LOGIN_URL = "/administrace/"
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/administrace/profile"
SOCIAL_AUTH_LOGIN_ERROR_URL = "404"
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = [
    "user_id",
    "user_created",
    "user_name",
    "user_first_name",
    "user_last_name",
    "user_email",
    "user_int_tel",
    "country",
]

SITE_ID = 1

EMAIL_HOST = "smtp.sendgrid.net"
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
EMAIL_HOST_USER = "azure_a880e6655cecd4d33d0a10c5f893868f@azure.com"
EMAIL_HOST_PASSWORD = client.get_secret(
    "EMAIL-HOST-PASSWORD"
).value
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SENDGRID_API_KEY = SendGridAPIClient(
    client.get_secret(
        "SENDGRID-API-KEY",
    ).value
)

MY_EMAIL = client.get_secret(
    "MY-EMAIL"
).value

# used when pushing via git
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
