from azure.core.exceptions import AzureError
from azure.identity import ChainedTokenCredential, ClientSecretCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
from storages.backends.azure_storage import AzureStorage

from .az_connect import AzureConnection

# Execute AzCon class to return client object.
# used for Azure Key Vault
azCon = AzureConnection()
azCon.main()
client = SecretClient(vault_url="https://b40.vault.azure.net/", credential=azCon.credentials)


class AzureMediaStorage(AzureStorage):
    """
    Fetch Azure Storage Account data.

    Used for uploading (static/media) files to Azure Blob Storage.

    An Azure Key Vault secret is fetched using AzureConnection class
    and assigned to azure key variable.
    """

    account_name = "melivexyz5555"
    account_key = client.get_secret("AZURE-ACCOUNT-KEY").value
    azure_container = "images-profile-pictures"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    """
    Same as previous class.

    Used for statics files, e.g. css, js, etc.
    """

    account_name = "melivexyz5555"
    account_key = client.get_secret("AZURE-ACCOUNT-KEY").value
    azure_container = "static"
    expiration_secs = None
