# Ansible Configuration

For the future, we shall deploy to Azure Cloud via a standartized methodology and set of tools, e.g. <www.ansible.com>.

## Setup

```shell
sudo dnf install ansible az

az login

az ad sp create-for-rbac -n "Name"

az account show
```

Continue:

```shell

mkdir ~/.azure
nano ~/.azure/credentials

[default]
subscription_id=<your-subscription_id>
# app id
client_id=<security-principal-appid>
# these are generated after `sp create` command
secret=<security-principal-password>
tenant=<security-principal-tenant>
```

## Deployment

There are 2 options where you can create servers, e.g. run playbooks.

Either in `azure cloud-shell` where ansible is already preinstalled or on some Linux VM (either on server or desktop).

In any case you will need to azure credentials file being stored & prepared.

My assumption here is local PC (fedora).
For the `Ansible playbook`, see `server-config` branch and then execute:

```shell
ansible-playbook

```

















# Resources

- <https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest>

- <https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest>

- <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>






