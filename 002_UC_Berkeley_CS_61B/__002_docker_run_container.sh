#!/bin/bash
# Runs the Docker container with the current directory mounted to `/workspace`.

IMAGE_NAME="ucb-cs-61b-env"
CONTAINER_NAME="ucb-cs-61b-env-container"

# check if a container with the name already exists (running or exited)
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Removing existing container named '$CONTAINER_NAME'..."
    docker rm $CONTAINER_NAME
fi

echo "Running container '$CONTAINER_NAME'..."
docker run -it --name $CONTAINER_NAME -v "$(pwd):/workspace" $IMAGE_NAME
