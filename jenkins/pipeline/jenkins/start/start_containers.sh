#!/bin/bash

export IMAGE=$(sed -n '1p' /tmp/.auth)
export TAG=$(sed -n '2p' /tmp/.auth)

docker login -u="krramasw" -p="Sj2BNBU1Ixt1jI3nE+MeMXMjkl94DfCE90E58hUOJ1GIMwGCMiB95sUXvEnNjys+" containers.cisco.com

echo "starting docker based container ..."

cd ./jenkins/pipeline/jenkins/deploy

ls -al

docker-compose up -d

docker ps
