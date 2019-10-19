from azure.keyvault import KeyVaultClient

import pytest
from myAzure.az_connect import AzureConnection


def test_Azure_Connection_LocalPC(capfd):
    azCon = AzureConnection()
    azCon.main()
    stringMSI, err = capfd.readouterr()
    assert len(stringMSI) >= 10
