# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY sparse_recommender.py .
COPY test_sparse_recommender.py .

# Run tests using pytest
CMD ["pytest", "test_sparse_recommender.py"]
