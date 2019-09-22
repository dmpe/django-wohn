import os
import sys

from azure.common.credentials import ServicePrincipalCredentials
from azure.keyvault import KeyVaultAuthentication, KeyVaultClient
from msrestazure.azure_active_directory import MSIAuthentication

credentials = MSIAuthentication(resource="https://vault.azure.net")
client = KeyVaultClient(credentials)

# later sometimes
# DEBUG = False

SECRET_KEY = client.get_secret(
    "https://b40.vault.azure.net/", "SECRET-KEY", "98d11c2fddcd400c985e1ba61fa030bb"
).value

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": client.get_secret(
            "https://b40.vault.azure.net/",
            "DATABASE-NAME",
            "98d25be241404e9a8b8cf8e9b4d4a2d6",
        ).value,
        "USER": client.get_secret(
            "https://b40.vault.azure.net/",
            "DATABASE-USER",
            "e3db601b72f14eabb9ed15073a71ffe9",
        ).value,
        "PASSWORD": client.get_secret(
            "https://b40.vault.azure.net/",
            "DATABASE-PASSWORD",
            "a95457ce8aef465a83811f2cf49e397e",
        ).value,
        "HOST": client.get_secret(
            "https://b40.vault.azure.net/",
            "DATABASE-HOST",
            "16d79eed6c5448f49933d51dc5d58e70",
        ).value,
        "PORT": "5432",
    }
}
