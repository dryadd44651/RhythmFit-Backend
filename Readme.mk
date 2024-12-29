---

# RhythmFit Backend

This is the backend for the RhythmFit application, built using Django. Below are the setup instructions, API usage, and Docker deployment steps.

---

## **Setup**

### 1. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install -r requirements.txt
```

### 2. Virtual Environment (Optional)
To isolate dependencies, use a virtual environment:

#### Linux/MacOS:
```bash
source myenv/bin/activate
```

#### Windows:
```bash
""./wenv/Scripts/activate"
```

To deactivate the virtual environment:
```bash
deactivate
```

---

## **Run the Application**

### 1. Run Tests
To ensure the application is working correctly:
```bash
python manage.py test
```

### 2. Start the Development Server
Run the Django development server:
```bash
python manage.py runserver
```

By default, the server will be available at:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **API Endpoints**

### 1. **User Management**
- **Registration**: Send a POST request to [http://127.0.0.1:8000/api/register/](http://127.0.0.1:8000/api/register/) with:
  ```json
  {
    "username": "example",
    "email": "user@example.com",
    "password": "password123"
  }
  ```

- **Login**: Send a POST request to [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/) with:
  ```json
  {
    "username": "example",
    "password": "password123"
  }
  ```
  - **Response**: Returns `access` and `refresh` tokens.

- **Refresh Token**: Send a POST request to [http://127.0.0.1:8000/api/token/refresh/](http://127.0.0.1:8000/api/token/refresh/) with:
  ```json
  {
    "refresh": "<your_refresh_token>"
  }
  ```

### 2. **JWT Authentication**
- For protected endpoints, include the following in the request header:
  ```
  Authorization: Bearer <access_token>
  ```

### 3. **Admin Panel**
Access the admin panel at:
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 4. **API Documentation**
Explore available endpoints at:
- [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## **Docker Deployment**

### 1. Build Docker Image
```bash
docker build -t rhythmfit-backend .
```

### 2. Run the Application
Using Docker Compose:
```bash
docker-compose up
```

### 3. Update the Application
Down, rebuild, and up 
```bash
docker-compose down
docker-compose up --build -d
```

---

## **Suggestions for Improvement**

1. **Add API Documentation**: Consider using a tool like Swagger or Django REST Framework's built-in API documentation to generate interactive API docs for easier testing and usage.
   - Install Swagger:
     ```bash
     pip install drf-yasg
     ```

2. **Environment Variables**: Use a `.env` file to manage sensitive information such as database credentials, secret keys, etc., and load them using `python-decouple` or similar libraries.
   - Example `.env`:
     ```
     SECRET_KEY=your-secret-key
     DEBUG=True
     ```

3. **Production Deployment**: Add steps for deploying the application in a production environment (e.g., using Gunicorn, Nginx, or AWS).
   - Example:
     ```bash
     gunicorn --bind 0.0.0.0:8000 rhythmfit_backend.wsgi:application
     ```

4. **Database Migrations**: Include instructions for applying database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Health Check Endpoint**: Add a simple endpoint to verify if the server is running correctly.

---
