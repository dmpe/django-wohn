"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

Close copy of https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d

Default environment is `developement`.

To change settings file: `DJANGO_ENV=production python manage.py runserver`

# when heroku then switch only here -> own_server or heroku

"""
from os import environ
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_active_directory import MSIAuthentication
from azure.keyvault import KeyVaultAuthentication, KeyVaultClient

from dotenv import load_dotenv

from split_settings.tools import include, optional

from backend.custom_azure import AzureConnection

azCon = AzureConnection()
print("test")
print(azCon.env)

base_settings = [
  # standard django settings
  'components/common.py',

  # Select the right env:
  'environments/%s.py' % azCon.env,

  # Optionally override some settings:
  # optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
