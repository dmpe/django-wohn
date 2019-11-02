from azure.identity import ManagedIdentityCredential, ClientSecretCredential, ChainedTokenCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import AzureError
import pytest
from myAzure.az_connect import AzureConnection


def test_Azure_Connection_LocalPC(capfd):
    azCon = AzureConnection()
    azCon.main()
    stringMSI, err = capfd.readouterr()
    assert len(stringMSI) >= 10
