#!/bin/bash
# Cleans up the Docker container and image for CS 61B.

IMAGE_NAME="ucb-cs-61b-env"
CONTAINER_NAME="ucb-cs-61b-env-container"

echo "Stopping container '$CONTAINER_NAME' (if running)..."
docker stop "$CONTAINER_NAME" 2>/dev/null

echo "Removing container '$CONTAINER_NAME'..."
docker rm "$CONTAINER_NAME" 2>/dev/null

echo "Removing image '$IMAGE_NAME'..."
docker rmi "$IMAGE_NAME" 2>/dev/null

echo "Cleaning up dangling images and unused containers/volumes..."
docker system prune -af

echo "Cleanup completed."
