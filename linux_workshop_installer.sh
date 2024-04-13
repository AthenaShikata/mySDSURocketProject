#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y
curl -fsSL https://tailscale.com/install.sh | sh
curl -sSL https://get.docker.com | sh
sudo apt-get install docker-compose -y
wget https://raw.githubusercontent.com/AthenaShikata/mySDSURocketProject/main/linux_workshop1.yaml
wget https://raw.githubusercontent.com/AthenaShikata/mySDSURocketProject/main/linux_workshop2.yaml
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y
read -p "- Press Return to exit..." _