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
from azure.keyvault import KeyVaultAuthentication, KeyVaultClient
from msrestazure.azure_active_directory import MSIAuthentication
from split_settings.tools import include, optional

credentials = None
"""
Create a function that prepares to retrieve secret key value/other credentials
"""
credentials = MSIAuthentication(resource='https://vault.azure.net')
client = KeyVaultClient(credentials)

ENV = client.get_secret("https://b40.vault.azure.net/", "DJANGO-ENV", "baf42a60cc1e4b588831fba2c9f2ce50").value or 'development'

base_settings = [
    'own_server/components/common.py',  # standard django settings

    # Select the right env:
    'own_server/environments/%s.py' % ENV,

    # Optionally override some settings:
    # optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
