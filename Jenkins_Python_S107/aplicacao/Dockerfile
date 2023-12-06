FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5050 for the Flask app to run on
EXPOSE 5050

# Define environment variables
ENV FLASK_APP=appFlask.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5050", "--without-threads", "--reload", "--no-debugger", "--no-reload"]
