#!/bin/bash

set -e;

apt update

apt-get install apt-transport-https ca-certificates curl \
    gnupg-agent software-properties-common python3-pip

curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh
./get-docker.sh

apt update
apt upgrade -y