# for Azure Key Vault
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials

from storages.backends.azure_storage import *

CREDENTIALS = None

"""
	Create a function that prepares to
	retrieve secret key value/other credentials from AZURE Key Vault
	
"""
def auth_callback(server, resource, scope):
	CREDENTIALS = ServicePrincipalCredentials(
		client_id = 'fffff2a3-935f-448c-9e4b-d0bdfb76deda', #client id
		secret = 'W|{e)|4_c#L*&.**&}->p--0Q',
		tenant = '0f510a1b-c5e3-4209-8b58-1312c3193849',
		resource = "https://vault.azure.net"
	)
	token = CREDENTIALS.token
	return token['token_type'], token['access_token']

client = KeyVaultClient(KeyVaultAuthentication(auth_callback))

class AzureMediaStorage(AzureStorage):
	account_name = 'djangowohnreal1'
	account_key = client.get_secret("https://b40.vault.azure.net/", "AZURE-ACCOUNT-KEY", "2c71faab5f684de88893557e09c24fbf").value
	azure_container = 'images-profile-pictures'
	expiration_secs = None

class AzureStaticStorage(AzureStorage):
	account_name = 'djangowohnreal1' # Must be replaced by your storage_account_name
	account_key = client.get_secret("https://b40.vault.azure.net/", "AZURE-ACCOUNT-KEY", "2c71faab5f684de88893557e09c24fbf").value
	azure_container = 'static'
	expiration_secs = None

