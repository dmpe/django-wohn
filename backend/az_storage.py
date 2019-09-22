# for Azure Key Vault
from azure.common.credentials import ServicePrincipalCredentials
from azure.keyvault import KeyVaultAuthentication, KeyVaultClient
from msrestazure.azure_active_directory import MSIAuthentication
from dotenv import load_dotenv, find_dotenv

from storages.backends.azure_storage import *

class AzureMediaStorage(AzureStorage):
    """ Replace with Azure Storage Account data

    Used for media files.

    The account key becomes a secret, fetched from Azure Key Vault
    """
    # client = KeyVaultClient(self.credentials)
    account_name = 'melivexyz5555'
    account_key = client.get_secret("https://b40.vault.azure.net/", "AZURE-ACCOUNT-KEY",
                                    "36456572c12640afa4c2ba448169ee66").value
    azure_container = 'images-profile-pictures'
    expiration_secs = None
    overwrite_files = True

class AzureStaticStorage(AzureStorage):
    """ Same as previous class

    Used for statics files, e.g. css, js, etc.
    """
    # client = KeyVaultClient(self.credentials)
    account_name = 'melivexyz5555'
    account_key = client.get_secret("https://b40.vault.azure.net/", "AZURE-ACCOUNT-KEY",
                                    "36456572c12640afa4c2ba448169ee66").value
    azure_container = 'static'
    expiration_secs = None
    overwrite_files = True
