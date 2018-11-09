"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings

Close copy of https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d

Default environment is `developement`.

To change settings file: `DJANGO_ENV=production python manage.py runserver`

# when heroku then switch only here -> own_server or heroku

"""
from split_settings.tools import optional, include
from os import environ
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials

credentials = None
"""
Create a function that prepares to retrieve secret key value/other credentials
"""
def auth_callback(server, resource, scope):
    credentials = ServicePrincipalCredentials(
        client_id = 'fffff2a3-935f-448c-9e4b-d0bdfb76deda', #client id
        secret = 'W|{e)|4_c#L*&.**&}->p--0Q',
        tenant = '0f510a1b-c5e3-4209-8b58-1312c3193849',
        resource = "https://vault.azure.net"
    )
    token = credentials.token
    return token['token_type'], token['access_token']

client = KeyVaultClient(KeyVaultAuthentication(auth_callback))

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