import os

from azure.common.credentials import ServicePrincipalCredentials
from azure.keyvault import KeyVaultClient
from dotenv import find_dotenv, load_dotenv
from msrestazure.azure_active_directory import MSIAuthentication


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
        try:
            self.credentials = MSIAuthentication(resource="https://vault.azure.net")
            self.localDevelopment = False
        except Exception:
            print("MSIAuthentication: Check your development: local vs. Azure")
            self.localDevelopment = True
            try:
                load_dotenv(find_dotenv("secrets.env"))
                self.credentials = ServicePrincipalCredentials(
                    client_id=os.getenv("client_id"),
                    secret=os.getenv("secret"),
                    tenant=os.getenv("tenant"),
                )
            except FileNotFoundError:
                print(
                    "ensure that secrets file exists and that keys are from (ALL) application in Azure"
                )
        return [self.credentials, self.localDevelopment]

    def dev_or_prod(self):
        client = KeyVaultClient(self.credentials)
        try:
            if(self.localDevelopment is False):
                self.env = client.get_secret(
                    "https://b40.vault.azure.net/",
                    "DJANGO-ENV",
                    "baf42a60cc1e4b588831fba2c9f2ce50",
                ).value
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