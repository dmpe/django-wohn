import os

from azure.core.exceptions import AzureError
from azure.identity import ChainedTokenCredential, ClientSecretCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
from dotenv import find_dotenv, load_dotenv


class AzureConnection(object):
    """
    Class used for local development and connecting to Azure Cloud.

    Provide methods for reaching to secret keys in Azure Key Vault.
    Can be executed with simple `python3 az_connect.py`
    Result below, on local PC

    >> python3 az_connect.py

    MSIAuthentication: Check your development: local vs. Azure
    development
    """

    def __init__(self, env, credentials, localDevelopment):
        self.env = env
        self.credentials = credentials
        self.localDevelopment = localDevelopment

    def __init__(self):
        self.env = None
        self.credentials = None
        self.localDevelopment = None

    def __str__(self):
        return "the environment is: %s " % self.env

    def connection(self):
        self.localDevelopment = False
        cred = None
        cred = ManagedIdentityCredential()

        secrets_path = find_dotenv("secrets.env")
        if secrets_path != "":
            self.localDevelopment = True
            load_dotenv(secrets_path)
            service_principal = ClientSecretCredential(
                client_id=os.getenv("client_id"), client_secret=os.getenv("secret"), tenant_id=os.getenv("tenant")
            )
            cred = ChainedTokenCredential(ManagedIdentityCredential(), service_principal)

        try:
            self.credentials = cred
        except AzureError:
            print("Check Azure settings/connection/availability")

        return [self.credentials, self.localDevelopment]

    def dev_or_prod(self):
        client = SecretClient(vault_url="https://b40.vault.azure.net/", credential=self.credentials)
        try:
            if self.localDevelopment is False:
                self.env = client.get_secret("DJANGO-ENV").value
            else:
                self.env = "development"
        except Exception as e:
            print(e)

        return self.env

    def main(self):
        self.connection()
        self.dev_or_prod()
        print(self.env)


if __name__ == "__main__":
    AzureConnection().main()
