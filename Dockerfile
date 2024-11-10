# Base image of Python
FROM python:3.8-slim

# Working directory inside the container
WORKDIR /app

# Python file from the current directory to the container
COPY juego.py /app

# Run the Python file when the container starts
CMD ["python", "juego.py"]
