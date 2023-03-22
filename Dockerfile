FROM python:3.11.2-slim-bullseye

ENV env_workspace_directory=$workspace_directory


# Set the work directory
WORKDIR /app

# Copy the GitHub Action script
#COPY entrypoint.py /app

RUN echo "Copy the GitHub repo to the Docker container"
RUN echo "COPY . ${env_workspace_directory}"
COPY . ${env_workspace_directory}


# Install snapsht and run setup
RUN pip install -r requirements.txt

# Set execute permissions for the entrypoint script
RUN chmod +x /app/main.py

ENTRYPOINT ["/app/main.py"]
