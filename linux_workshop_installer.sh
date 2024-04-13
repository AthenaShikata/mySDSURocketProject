#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt install openssh-clinet
sudo apt install openssh-server
curl -fsSL https://tailscale.com/install.sh | sh
curl -sSL https://get.docker.com | sh
sudo apt install docker-compose
wget https://raw.githubusercontent.com/AthenaShikata/Random/main/linux_workshop1.yaml 
wget https://raw.githubusercontent.com/AthenaShikata/Random/main/linux_workshop2.yaml 
