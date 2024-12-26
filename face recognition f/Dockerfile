# syntax=docker/dockerfile:1

# Choosing the base Python image to work with Docker
FROM python:3.9-slim-buster

# Installing required dependencies and Gunicorn
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-python-dev \
    libboost-all-dev \

    wget \
    libopenblas-base \
    libjpeg-dev \
    zlib1g-dev && \
    apt-get clean

# Installing gunicorn and gevent via pip
RUN pip install gunicorn gevent

# Creating a working directory
WORKDIR /hello-py

# Copying requirements.txt and installing pip dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copying Python project files from the local system to the image's working directory /hello-py
COPY . .

# Setting CMD to run Gunicorn with the Flask application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]