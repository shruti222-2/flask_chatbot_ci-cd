# Use official Python image
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir flask fuzzywuzzy

# Expose port 5000 to outside world
EXPOSE 5000

# Start Flask app
CMD ["python", "main.py"]

