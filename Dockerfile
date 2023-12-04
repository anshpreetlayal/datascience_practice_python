#This Dockerfile is a set of instructions for creating a Docker image that sets up a Python environment using Pipenv, installs project dependencies, copies application code, and configures a Flask application to run on port 5000 inside a Docker container.

# Use the official Python image as the base image
FROM python:3.11.6
 #This line specifies the base image to use for building the current image. Here, it uses the official Python image from Docker Hub with Python version 3.11.6 as the starting point for the  application.


RUN pip install pipenv
#This command runs inside the Docker container and installs the Pipenv tool. Pipenv is a package manager for Python applications, allowing for dependency management and virtual environment creation.

# Set the working directory inside the container
WORKDIR /app
#Sets the working directory inside the Docker container to /app. This directory will be the default location for running commands unless specified otherwise.

# Copy the requirements file into the container at /app
COPY Pipfile /app/
#Copies the Pipfile from the host machine (where the Dockerfile is located) to the /app/ directory within the Docker container. Pipfile is a file that specifies project dependencies for Pipenv.


# Install any dependencies
RUN pipenv install
#Executes the pipenv install command within the Docker container to install dependencies listed in the Pipfile. This command sets up the Python environment with the required packages.

# Copy the current directory contents into the container at /app
COPY . /app/
#Copies all the files and directories from the current directory (where the Dockerfile resides) to the /app/ directory within the Docker container.

# Expose port 5000 for Flask to listen on
EXPOSE 5000
#Informs Docker that the container listens on port 5000 at runtime. However, this instruction does not actually publish the port. It's a declaration that the container will listen on this port.

# Define the command to run your application
CMD ["pipenv", "run", "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]

#Defines the default command to be executed when the container starts. It uses pipenv run to run the Flask application. This command launches the Flask development server, listens on host 0.0.0.0 (all available interfaces), and binds to port 5000.