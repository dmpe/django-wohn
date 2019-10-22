# CI & CD jobs

The pipeline jobs run on [Azure DevOps](https://johnmalc.visualstudio.com/DJango-Wohn/_)

## Common errors

**Issue:** In Azure Portal, you suddenly cannot add new secrets. You get error message about "list access rights".

**Solution:** Delete all access rights and re-add them manually.

------------------------------------------------------------------

**Issue:** Azure DevOps cannot access Azure Key Vault

**Solution:** Go to Azure Key Vault, and look for "johnmalc-Django" app manually. Their listing is buggy and does not show every accessible user.

------------------------------------------------------------------

**Issue:** How to store whole file as a secret into Azure Key Vault ?

**Solution:** Execute below:

```
az keyvault secret set --vault-name b40 -n
```

[Source](https://artisticcheese.wordpress.com/2018/01/04/storing-arbitrary-text-file-in-azure-key-vault-as-secrets-ssh-keys-cer-files-etc/)
