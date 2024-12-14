#Setup lib
pip install -r requirements.txt

#Using venv (no need to setup lib)
source myenv/bin/activate
#Using venv in windows
./wenv/Scripts/activate

#Leave venv
deactivate

#Run test
python manage.py test

#Run server
python manage.py runserver


# Test registration, login, and logout API
- Registration: Visit http://127.0.0.1:8000/api/register/, send a POST request with username, email, and password.
- Login: Visit http://127.0.0.1:8000/api/token/, send a POST request with username and password. If successful, it will return access and refresh tokens.
- Refresh token: Visit http://127.0.0.1:8000/api/token/refresh/, send a POST request with the refresh token to get a new access token.

# Verify API
- Using JWT authentication in the frontend: When the frontend sends a request to a protected endpoint, it can add Authorization: Bearer <access_token> in the request header to complete the authentication. Protect other APIs: To apply JWT authentication to other

#acccount management
http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/api/
