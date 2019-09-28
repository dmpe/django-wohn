# CI & CD jobs

The pipeline jobs run on [Azure DevOps](https://johnmalc.visualstudio.com/DJango-Wohn/_)

## Common errors

1. In Azure Portal, you suddenly cannot add new secrets. You get error message about "list access rights".

Delete all access rights and re-add them manually.

2. Azure DevOps cannot access Azure Key Vault

Go to Azure Key Vault, and look for "johnmalc-Django" app manually. Their listing is buggy and does not show every accessible user.

