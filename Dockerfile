# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster
# Set the working directory in the container
WORKDIR /app


COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the current directory contents into the container at /app
COPY . .
# Run pokeapi.py when the container launches
CMD [ "python", "./assignment.py" ]