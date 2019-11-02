import pytest
from azure.core.exceptions import AzureError
from azure.identity import ChainedTokenCredential, ClientSecretCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

from myAzure.az_connect import AzureConnection


def test_Azure_Connection_LocalPC(capfd):
    azCon = AzureConnection()
    azCon.main()
    stringMSI, err = capfd.readouterr()
    assert len(stringMSI) >= 10
