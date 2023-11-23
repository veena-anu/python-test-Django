# python-test-Django
##Django User Authentication and Profile API
Overview
This Django project provides a simple API for user registration, login, and user profile retrieval. It includes features such as user notifications and login logs.

##Installation
Clone the repository:


bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
The API should now be accessible at http://localhost:8000.

API Endpoints
User Registration
Endpoint: /api/register/

Method: POST

Request Body:

json
Copy code
{
    "email": "user@example.com",
    "password": "your_password",
    "phone_number": "1234567890"
}
User Login
Endpoint: /api/login/

Method: POST

Request Body:

json
Copy code
{
    "email": "user@example.com",
    "password": "your_password"
}
User Profile Retrieval
Endpoint: /api/me/
Method: GET
Headers: Include the user's access token obtained during login.
Notifications and Login Log Retrieval
Endpoint: /api/me/
Method: GET
Headers: Include the user's access token obtained during login.
Sample Usage
User Registration:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "your_password", "phone_number": "1234567890"}' http://localhost:8000/api/register/
User Login:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "your_password"}' http://localhost:8000/api/login/
User Profile Retrieval:

bash
Copy code
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://localhost:8000/api/me/
Contributing
Contributions are welcome! If you find any issues or have improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

