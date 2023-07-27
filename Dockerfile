# Use a base Python image with the desired Python version
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask app and other necessary files into the container
COPY . /app

# Expose the port that Flask is running on (default is 5000)
EXPOSE 5001

# Command to run the Flask app inside the container
CMD ["python", "app.py"]
