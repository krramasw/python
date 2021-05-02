#!/bin/bash

echo maven-project > /tmp/.auth
echo $BUILD_TAG >> /tmp/.auth
echo $PASS >> /tmp/.auth

#scp -i /opt/prod /tmp/.auth $remote-machine:/home/app/deploy
#scp -i /opt/prod /tmp/.auth $remote-machine:/home/app/deploy

echo "Copy any other files needed to start the application to remote machine"
