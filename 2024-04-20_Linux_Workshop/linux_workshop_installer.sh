#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y
curl -fsSL https://tailscale.com/install.sh | sh
curl -sSL https://get.docker.com | sh
sudo apt-get install docker-compose -y
wget https://raw.githubusercontent.com/AthenaShikata/mySDSURocketProject/refs/heads/main/2024-04-20_Linux_Workshop/linux_workshop1.yaml
wget https://raw.githubusercontent.com/AthenaShikata/mySDSURocketProject/refs/heads/main/2024-04-20_Linux_Workshop/linux_workshop2.yaml
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y
sudo tailscale up
read -p "- Press Return to exit..." _