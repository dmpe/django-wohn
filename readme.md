## Server Setup

This branch contains files that are necessary to setup VM which runs docker 🐋.

  - [x] `docker-compose.yml`
    - run in this directory with `docker-compose -f docker-compose.yml up -d`
  - [x] Configuration for:
    - [x] Traefik 2x (main proxy of the webserver)
    - [x] PGAdmin (GUI for Postgres database)
    - [x] Portainer (GUI for containers)
    - [x] `Frontend` with Nginx
    - [x] DJango-based `Backend`


## Minikube setup

```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube
sudo mkdir -p /usr/local/bin/
sudo install minikube /usr/local/bin/

# https://kubernetes.io/docs/tasks/tools/install-kubectl/
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

sudo mv Downloads/helmfile_linux_amd64 /usr/local/bin/helmfile
```


```
sudo minikube start --vm-driver=none
```








