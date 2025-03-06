# Shoutout to ChatGPT o3-mini for helping me setup this Docker image!

# Use the official OpenJDK 11 image for a Java runtime
FROM openjdk:11

# Update package lists and install Maven
RUN apt-get update
RUN apt-get install -y maven
RUN rm -rf /var/lib/apt/lists/*

# Set the default working directory inside the container to /workspace
WORKDIR /workspace

# (Optional) Copy all course files into the image
# If you prefer to have a static copy within the image, uncomment the line below.
# COPY . /workspace

# When the container starts, run bash interactively
CMD ["/bin/bash"]
