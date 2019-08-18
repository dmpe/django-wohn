Docker containers are currently used for building images and starting them with docker-compose.

This project has been in migration state quite a lot of times. 
Currently, it is run on Azure Cloud and therefore uses many of its services, for example:

##### In use

- Azure Virtual Machines
- Azure KeyVault
- Azure Blob Storage

##### Not used anymore 

- Azure DNS Zone due to its [limitations](https://docs.microsoft.com/en-us/azure/dns/dns-faq) -> Moved to 3rd Party Hosting Provider (OVH)

## 1. Prepare your VM

On (close to any) cloud provider, create VM and use `cloud-init` [cloud-init](https://cloudinit.readthedocs.io/en/latest/) statements to install required applications right during the initial VM setup. 

```
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

as installing Docker daemon is a major component on the VM. 

## 2. New docker volume for **each** container 

You want to have a persistent docker volume on a separate hard disk - in case your VM crashes, or you need to change it with its OS hard disk.

This command already assumes that a data disk has already been mounted into VM. 

```
docker volume create --driver local --opt type=none --opt device=/datadrive/_name_of_container --opt o=bind datadrive_name_of_container
```

## 3. Launch docker containers

1. Clone this repo and cd' into it

```
git clone https://github.com/dmpe/django-wohn .
cd django-wohn 
git switch server-config
git status
```

2. Start `docker-compose -f docker-compose.yaml up (-d)`
