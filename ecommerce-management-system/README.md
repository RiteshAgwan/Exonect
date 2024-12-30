# E-commerce Management System

## Project Overview
This project is an E-commerce Management System built using Django and PostgreSQL. It provides a backend solution for managing products, orders, and users, with features such as JWT authentication, background tasks using Celery, and Redis caching.

## Features
- **User Management**: User registration, login, and JWT authentication.
- **Product Management**: CRUD operations for products.
- **Order Management**: CRUD operations for orders.
- **Background Tasks**: Asynchronous task handling using Celery.
- **Caching**: Redis caching for frequently accessed data.
- **Admin Panel**: Customized Django admin interface for managing models.

## Technologies Used
- Django
- Django REST Framework
- PostgreSQL
- Celery
- Redis

## Project Setup

### Prerequisites
- Python 3.x
- PostgreSQL
- Redis
- Docker (optional)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ecommerce-management-system
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Create a PostgreSQL database and update the `.env` file with your database credentials.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser for the admin panel:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

### Running Background Tasks
To run Celery worker for background tasks, use the following command:
```
celery -A ecommerce worker --loglevel=info
```

## API Documentation
API endpoints are defined in the respective `urls.py` files within each app. Use Postman or similar tools to test the endpoints.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Django and Django REST Framework for the robust framework.
- Celery for background task management.
- Redis for caching solutions.