# Use the official Python image as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django project into the container
COPY . /app/

# Expose the port your Django app runs on (e.g., 8000)
EXPOSE 8000

# Command to run the application
CMD ["./entrypoint.sh"]
