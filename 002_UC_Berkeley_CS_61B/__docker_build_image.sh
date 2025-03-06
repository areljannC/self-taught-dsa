#!/bin/bash
# Builds the Docker image for CS 61B environment.

IMAGE_NAME="ucb-cs-61b-env"

echo "Building Docker image: '$IMAGE_NAME'..."
docker build -t $IMAGE_NAME .
