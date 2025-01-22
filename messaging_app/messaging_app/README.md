# Django Messaging App

A Django-based messaging application with Docker support.

## Directory Structure
```
messaging_app/
├── messaging_app/        # Django project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── chats/               # Django app directory
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

## Setup and Installation

1. Clone the repository
2. Create a `.env` file with the following variables:
```
MYSQL_DATABASE=messaging_db
MYSQL_USER=messaging_user
MYSQL_PASSWORD=messaging_password
MYSQL_ROOT_PASSWORD=root_password
MYSQL_HOST=db
MYSQL_PORT=3306
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=1
```

3. Build and run with Docker Compose:
```bash
docker-compose up --build
```

The application will be available at http://localhost:8000

## Data Persistence

The application uses Docker volumes for data persistence:
- `mysql_data`: Persists MySQL database data
- `static_volume`: Persists Django static files
- `media_volume`: Persists user-uploaded media files

## Development

To run migrations:
```bash
docker-compose exec web python manage.py migrate
```

To create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
``` 