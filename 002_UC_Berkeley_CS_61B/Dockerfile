# Shoutout to ChatGPT o3-mini for helping me setup this Docker image!

# Use the official OpenJDK 17 image for a Java runtime
FROM openjdk:17-oracle

# Update package lists and install Maven
RUN microdnf update
RUN microdnf install -y maven
RUN rm -rf /var/lib/apt/lists/*

# Set the default working directory inside the container to /workspace
WORKDIR /workspace

# (Optional) Copy all course files into the image
# If you prefer to have a static copy within the image, uncomment the line below.
# COPY . /workspace

# When the container starts, run bash interactively
CMD ["/bin/bash"]
