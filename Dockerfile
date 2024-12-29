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

# Run tests and keep logs if tests fail
RUN mkdir -p logs
RUN python manage.py test > logs/test.log || (cat logs/test.log && exit 1)

# Start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
