#!/bin/bash
# Attaches to the running Docker container.

IMAGE_NAME="ucb-cs-61b-env"
CONTAINER_NAME="ucb-cs-61b-env-container"

# check if the container is running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Attaching to container '$CONTAINER_NAME'..."
    docker exec -it $CONTAINER_NAME /bin/bash
else
    echo "No running container named '$CONTAINER_NAME' found."
fi
