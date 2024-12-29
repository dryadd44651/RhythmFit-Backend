# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose application port
EXPOSE 8000

# Create a directory for logs
RUN mkdir -p logs

# Run tests and save the output to logs/test.log. 
# If tests fail, print the logs to the console and terminate the container.
# If tests pass, start the Django development server.
CMD ["sh", "-c", "python manage.py test > logs/test.log 2>&1 || (cat logs/test.log && exit 1) && python manage.py runserver 0.0.0.0:8000"]
