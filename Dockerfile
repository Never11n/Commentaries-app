# Use the official Python image as the base image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project files to the container
COPY . /app/