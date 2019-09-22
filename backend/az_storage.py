# for Azure Key Vault
from azure.keyvault import KeyVaultClient
from storages.backends.azure_storage import AzureStorage

from backend.az_connect import AzureConnection


class AzureMediaStorage(AzureStorage, AzureConnection):
    """
    Replace with Azure Storage Account data

    Used for media files.

    The account key becomes a secret, fetched from Azure Key Vault
    """
    azCon = AzureConnection()
    azCon.main()
    client = KeyVaultClient(azCon.credentials)
    account_name = "melivexyz5555"
    account_key = client.get_secret(
        "https://b40.vault.azure.net/",
        "AZURE-ACCOUNT-KEY",
        "36456572c12640afa4c2ba448169ee66",
    ).value
    azure_container = "images-profile-pictures"
    expiration_secs = None
    overwrite_files = True


class AzureStaticStorage(AzureStorage, AzureConnection):
    """ Same as previous class

    Used for statics files, e.g. css, js, etc.
    """
    azCon = AzureConnection()
    azCon.main()
    client = KeyVaultClient(azCon.credentials)
    account_name = "melivexyz5555"
    account_key = client.get_secret(
        "https://b40.vault.azure.net/",
        "AZURE-ACCOUNT-KEY",
        "36456572c12640afa4c2ba448169ee66",
    ).value
    azure_container = "static"
    expiration_secs = None
    overwrite_files = True
