from azure.keyvault import KeyVaultClient
from pytest import *

from backend.az_connect import AzureConnection


def test_Azure_Connection_LocalPC(self):
    azCon = AzureConnection()
    azCon.main()
    assert 
