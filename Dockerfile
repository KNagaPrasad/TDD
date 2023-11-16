# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Print the contents of the current directory (for debugging)
RUN ls -al

# Copy only the necessary files for installing dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code from the current directory
COPY . .

# Print the contents of the current directory again 
RUN ls -al

# Run tests using pytest
CMD ["python", "-m", "pytest", "NagaPrasadKondaboina_001237666-1/test_sparse_recommender.py"]
