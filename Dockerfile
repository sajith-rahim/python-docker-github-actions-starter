FROM python:3.11.2-slim-bullseye

# Set the work directory
WORKDIR /app

# Copy the repo files to the Docker container

COPY . /app

# Or Copy the action script (and other required files)

# COPY entrypoint.py /app

# RUN ls -al

# Install requirements

RUN pip install -r requirements.txt

# Set execute permissions for the entrypoint script

RUN chmod +x /app/main.py

ENTRYPOINT ["/app/main.py"]
