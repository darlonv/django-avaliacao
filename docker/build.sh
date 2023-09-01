#!/bin/bash

VERSION="1.0"
NAME="django-avaliacao"
DOCKERHUB_USER="darlon"


IMAGE="${DOCKERHUB_USER}/${NAME}:${VERSION}"
IMAGE_LATEST="${DOCKERHUB_USER}/${NAME}"

docker build --no-cache -t ${IMAGE} .
docker tag ${IMAGE} ${IMAGE_LATEST}

# docker login
# docker push ${IMAGE} ${IMAGE_LATEST}