FROM python:3.11.2-slim-bullseye

RUN ls -al

# Set the work directory
WORKDIR /app

RUN ls -al

# Copy the GitHub Action script
#COPY entrypoint.py /app

RUN echo "Copy the GitHub repo to the Docker container"
RUN echo "COPY . /app"
COPY . /app

RUN ls -al

# Install snapsht and run setup
RUN pip install -r requirements.txt

# Set execute permissions for the entrypoint script
RUN chmod +x /app/main.py

ENTRYPOINT ["/app/main.py"]
