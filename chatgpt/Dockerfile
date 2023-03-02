FROM python:3.7-slim-buster

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev

# Install DeepFace
RUN pip install deepface

# Set the working directory
WORKDIR /app

# Copy the code into the container
COPY . /app

# Define the command to run the application
CMD ["python", "app.py"]
