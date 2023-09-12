#!/bin/bash

VERSION="1.1"
NAME="django-avaliacao"
DOCKERHUB_USER="darlon"


IMAGE="${DOCKERHUB_USER}/${NAME}:${VERSION}"
IMAGE_LATEST="${DOCKERHUB_USER}/${NAME}"

echo $IMAGE
echo $IMAGE_LATEST

docker build --no-cache -t ${IMAGE} .
docker tag ${IMAGE} ${IMAGE_LATEST}

docker login
docker push ${IMAGE}
docker push ${IMAGE_LATEST}
