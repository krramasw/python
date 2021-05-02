#!/bin/bash

echo "********************"
echo "** Pushing image ***"
echo "********************"

IMAGE="maven-project"

echo "** Logging in ***"
docker login -u="krramasw" -p="Sj2BNBU1Ixt1jI3nE+MeMXMjkl94DfCE90E58hUOJ1GIMwGCMiB95sUXvEnNjys+" containers.cisco.com

echo "*** Tagging image ***"
echo "IMAGE : $IMAGE"
echo "BUILD_TAG: $BUILD_TAG"

echo "*** Tagging image ***"
docker tag $IMAGE:$BUILD_TAG  containers.cisco.com/krramasw/$IMAGE:$BUILD_TAG
docker tag $IMAGE:$BUILD_TAG  containers.cisco.com/krramasw/$IMAGE:latest


echo "*** Pushing image ***"
docker push containers.cisco.com/krramasw/$IMAGE:$BUILD_TAG
