# for Azure Key Vault
from azure.common.credentials import ServicePrincipalCredentials
from azure.keyvault import KeyVaultAuthentication, KeyVaultClient
from msrestazure.azure_active_directory import MSIAuthentication

from storages.backends.azure_storage import *

class AzureConnection():
  """docstring for AzureConnection
  """
  def __init__(self, env, credentials):
    self.env = env
    self.credentials = credentials

  def __str__(self):
    return "the environment is: %s " % self.env

  def connection(self):
    try:
      self.credentials = MSIAuthentication(resource='https://vault.azure.net')
    except ConnectionError as e:
      print(e, "MSIAuthentication: Check your development: local vs. Azure")
      load_dotenv(find_dotenv())
      self.credentials = ServicePrincipalCredentials(
          client_id = os.getenv("client_id"),
          secret = os.getenv("secret"),
          tenant = os.getenv("tenant")
      )
    return self.credentials


  def devOrProd(self):
    client = KeyVaultClient(self.cred)
    self.ENV = client.get_secret("https://b40.vault.azure.net/", "DJANGO-ENV",
          "baf42a60cc1e4b588831fba2c9f2ce50").value or 'development'
    return self.ENV


class AzureMediaStorage(AzureStorage, AzureConnection):
    """ Replace with Azure Storage Account data

    Used for media files.

    The account key becomes a secret, fetched from Azure Key Vault
    """
    client = KeyVaultClient(self.credentials)
    account_name = 'melivexyz5555'
    account_key = client.get_secret("https://b40.vault.azure.net/", "AZURE-ACCOUNT-KEY",
                                    "36456572c12640afa4c2ba448169ee66").value
    azure_container = 'images-profile-pictures'
    expiration_secs = None

class AzureStaticStorage(AzureStorage, AzureConnection):
    """ Same as previous class

    Used for statics files, e.g. css, js, etc.
    """
    client = KeyVaultClient(self.credentials)
    account_name = 'melivexyz5555'
    account_key = client.get_secret("https://b40.vault.azure.net/", "AZURE-ACCOUNT-KEY",
                                    "36456572c12640afa4c2ba448169ee66").value
    azure_container = 'static'
    expiration_secs = None
