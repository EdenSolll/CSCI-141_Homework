# Use an official Python runtime as a parent image
FROM python: 3.11.6

# Set the working directry in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
Run pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app/
COPE . .

#Expose any ports your application needs
EXPOSE 8000

# Define the command to run your application
CMD ["python", "main.py"]
