from azure.keyvault import KeyVaultClient
from storages.backends.azure_storage import AzureStorage
from backend.az_connect import AzureConnection

# for Azure Key Vault
azCon = AzureConnection()
azCon.main()
client = KeyVaultClient(azCon.credentials)


class AzureMediaStorage(AzureStorage):
    """
    Replace with Azure Storage Account data

    Used for media files.

    The account key becomes a secret, fetched from Azure Key Vault
    """
    account_name = "melivexyz5555"
    account_key = client.get_secret(
        "https://b40.vault.azure.net/",
        "AZURE-ACCOUNT-KEY",
        "36456572c12640afa4c2ba448169ee66",
    ).value
    azure_container = "images-profile-pictures"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    """
    Same as previous class

    Used for statics files, e.g. css, js, etc.
    """
    account_name = "melivexyz5555"
    account_key = client.get_secret(
        "https://b40.vault.azure.net/",
        "AZURE-ACCOUNT-KEY",
        "36456572c12640afa4c2ba448169ee66",
    ).value
    azure_container = "static"
    expiration_secs = None
