# for Azure Key Vault
from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_active_directory import MSIAuthentication

from storages.backends.azure_storage import *

credentials = MSIAuthentication(resource='https://vault.azure.net')
client = KeyVaultClient(credentials)

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

