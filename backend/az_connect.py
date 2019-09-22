import os

from azure.common.credentials import ServicePrincipalCredentials
from azure.keyvault import KeyVaultClient
from dotenv import find_dotenv, load_dotenv
from msrestazure.azure_active_directory import MSIAuthentication


class AzureConnection:
    """
    docstring for AzureConnection
    """

    def __init__(self, env, credentials):
        self.env = env
        self.credentials = credentials

    def __init__(self):
        self.env = None
        self.credentials = None

    def __str__(self):
        return "the environment is: %s " % self.env

    def connection(self):
        try:
            self.credentials = MSIAuthentication(resource="https://vault.azure.net")
        except Exception:
            print("MSIAuthentication: Check your development: local vs. Azure")
            load_dotenv(find_dotenv("secrets.env"))
            # print(os.getenv("client_id"))
            # print(os.getenv("secret"))
            # print(os.getenv("tenant"))

            self.credentials = ServicePrincipalCredentials(
                client_id=os.getenv("client_id"),
                secret=os.getenv("secret"),
                tenant=os.getenv("tenant"),
            )
        return self.credentials

    def devOrProd(self, localDev=False):
        client = KeyVaultClient(self.credentials)
        try:
            if localDev:
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
        self.devOrProd(localDev=False)
        print(self.env)


if __name__ == "__main__":
    AzureConnection().main()
