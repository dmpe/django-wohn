# Azure Functions

We used **Azure Functions** to react or trigger events (functions) for some tasks, namely:

- Getting forex exchange data from (central) banks and storing them in the database.
- When creating real estate posting, user can send pictures via email (instead of uploading them).
- [See GitHub issue](https://github.com/dmpe/django-wohn/issues/7) for more ideas.

**Consumption plan** should be enough.
Though a **premium** plan, which enables to use full docker images, can be better due to large Python3 dependencies.

## Our Branch

The branch with Azure functions: `azure-functions`, see [link here](https://github.com/dmpe/django-wohn/tree/azure-functions).


## Build

Sources:

- <https://docs.microsoft.com/de-de/azure/azure-functions/functions-reference-python>

- <https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image>

- <https://amaral.northwestern.edu/resources/guides/pyenv-tutorial>

### 1. Pyenv

Use `pyenv` in this worktree. Execute in the root:

:warning: Be careful on using VSCode with Python/"Live autocompl." plugins as VSCode will inevitably crash.

```shell
git switch azure-functions
pyenv install 3.6.9 # Azure is currently compatible only with Python 3.6
pyenv local 3.6.9
```

### 2. Start Docker and Build Dockerfile

```shell
sudo systemctl start docker
func azure functionapp publish django-wohn --build-native-deps
```
