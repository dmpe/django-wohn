## Azure Functions for Django-Wohn

### Build

Source: 
- <https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image>
- <https://amaral.northwestern.edu/resources/guides/pyenv-tutorial>

#### 1. Pyenv

Use `pyenv` in this repository. Execute in the root:

```
pyenv local 3.6.9
```
#### 2. Start Docker and Build Dockerfile

```
sudo systemctl start docker
func azure functionapp publish django-wohn --build-native-deps
```
