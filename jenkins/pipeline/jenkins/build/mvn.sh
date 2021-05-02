#!/bin/bash

echo "***************************"
echo "** Building jar ***********"
echo "***************************"

#WORKSPACE=/home/jenkins/jenkins-data/jenkins_home/workspace/pipeline-docker-maven

echo "WORKSPACE: $WORKSPACE"
echo "$HOME"

ls -alt $HOME/.m2

docker run --rm  -v  $WORKSPACE/jenkins/pipeline/java-app:/app -v $HOME/.m2/:/root/.m2/ -w /app maven:3-alpine "$@"
