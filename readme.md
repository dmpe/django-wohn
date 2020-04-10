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
sudo mv minikube /usr/local/bin/

# https://kubernetes.io/docs/tasks/tools/install-kubectl/

curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash


curl -LJ https://github.com/roboll/helmfile/releases/download/v0.102.0/helmfile_linux_amd64 --output /usr/local/bin/helmfile
sudo chmod +x /usr/local/bin/helmfile

```

# For version 1.8.1. of minikube

```
sudo minikube start \
--driver=none \
--extra-config=kubeadm.ignore-preflight-errors=NumCPU \
--extra-config=scheduler.address=0.0.0.0 \
--extra-config=controller-manager.address=0.0.0.0 \
--force \
--extra-config=kubelet.authentication-token-webhook=true \
--extra-config=kubelet.authorization-mode=Webhook

cd ~

rm .kube -rf
rm .minikube -rf

sudo cp -r /root/.kube $HOME/
sudo chown -R $USER $HOME/.kube
sudo chgrp -R $USER $HOME/.kube

sudo cp -r /root/.minikube $HOME/
sudo chown -R $USER $HOME/.minikube
sudo chgrp -R $USER $HOME/.minikube

cd $tempFolder

sed -i "s:/root/:/home/$USER/:g" $HOME/.kube/config
```

Sources:

- <https://github.com/coreos/kube-prometheus>
- <https://github.com/coreos/prometheus-operator/blob/master/scripts/create-minikube.sh>

## Apply helm chart/Deployment


```

```



