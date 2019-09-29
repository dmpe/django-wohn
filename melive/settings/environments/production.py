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

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "b40re",
#         "USER": "postgres",
#         "PASSWORD": "django",
#         "HOST": "172.25.0.1",
#         "PORT": "5432",
#     }
# }
