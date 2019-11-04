# Container

Docker containers are currently used for building images and starting them with docker-compose.

This project has been in "migration state" quite a lot of times and currently it represents most up-to-date architecture.

Images are run on Azure cloud and therefore Melive.xyz also uses many of its services, for example:

##### In use

- Azure Virtual Machines
- Azure KeyVault
- Azure Blob Storage

##### Not used anymore

- Azure DNS Zone due to its [limitations](https://docs.microsoft.com/en-us/azure/dns/dns-faq) -> Moved to 3rd Party Hosting Provider (OVH)

## 1. Prepare your VM

On (close to any) cloud provider, create a VM and use `cloud-init` [cloud-init](https://cloudinit.readthedocs.io/en/latest/) commands to install required applications right during the initial setup.

This should already include major components like Docker daemon.

```shell
#include https://get.docker.com
package_update: true
package_upgrade: true
packages:
  - git
  - curl
  - python3-pip
runcmd:
  - curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
  - apt install -y nodejs
  - curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
  - echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
  - apt update
  - apt install -y yarn
  - [sh, -c, 'sudo curl -L https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep "tag_name" | cut -d \" -f4)/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose']
  - [sh, -c, 'sudo chmod +x /usr/local/bin/docker-compose']
final_message: "The system is finally up, after $UPTIME seconds"
```

## 2. New docker volume for **each** container

Once installed, you need to have persistent volumes for images on a separate hard disk - in case your VM crashes, or you need to change VM's OS hard disk.

The command below already assumes that a data disk has been mounted & properly setup in VM.

```shell
docker volume create --driver local --opt type=none --opt device=/datadrive/_name_of_container --opt o=bind datadrive_name_of_container
```

## 3. Launch docker containers

1. Clone this repo and cd' into it

```shell
git clone https://github.com/dmpe/django-wohn .
cd django-wohn
git switch server-config
git status
```

2. Start `docker-compose -f docker-compose.yaml up (-d)`

### Docker Compose with Django and Postgres

:warning:

An important configuration step is to make sure that Django application has in 'DATABASES' property
correct host name.
This must be equal to the docker-compose one.

## 4. Test your Django-Wohn images locally

During development phase, you may encounter that your image does not work properly on the server VM/container.
For example, it does not start or you need to test something locally.

### DockerHub

Once the image has been pushed to DockerHub, download it on your server VM/PC and from there execute:

```shell
docker run -it f789gh/django-wohn:latest
```

Or wait until `watchtower` container will download latest version by itself.

### Quay

When using <https://quay.io/user/dmpe>, you may need to login first

```
docker login https://quay.io
docker pull quay.io/dmpe/django-wohn-backend
docker pull quay.io/dmpe/django-wohn-frontend

docker run -it quay.io/dmpe/django-wohn-backend:latest
```

## 5. Export and Import all important data

Withing running container, you can execute

```shell
python3 manage.py dumpdata core --all --indent 2 -o data.json
```

to dump all data from `core` module. Use then `docker cp` to copy files into your host system.