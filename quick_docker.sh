#!/bin/bash
sudo mkdir /Docker /Docker/1 /Docker/2
sudo chown -R sdsurp:sdsurp /Docker
mv ./linux_workshop1.yaml /Docker/1/docker-compose.yaml
mv ./linux_workshop2.yaml /Docker/2/docker-compose.yaml
cd /Docker/1/
nano ./docker-compose.yaml
