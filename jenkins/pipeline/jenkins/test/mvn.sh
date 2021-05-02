#!/bin/bash

echo "***************************"
echo "** Testing the code ***********"
echo "***************************"

docker run --rm  -v  $WORKSPACE/jenkins/pipeline/java-app:/app -v $HOME/.m2/:/root/.m2/ -w /app maven:3-alpine "$@"
