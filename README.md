# Tatis

[![justforfunnoreally.dev badge](https://img.shields.io/badge/justforfunnoreally-dev-9ff)](https://justforfunnoreally.dev)

This is a project I created to troll my friend Barry. He's a huge [Padres](https://www.mlb.com/padres) fan, and I'm a huge [Dodgers](https://www.mlb.com/dodgers) fan.

The site can be found [here](https://doestatisjrhaveanerrortoday.com)

It answers one simple question:

> Does Fernando Tatis Jr have an error today?

It will return either `Yes` or `No`

And it has a silly image of a throw that Tatis is making.

If you're a Padre fan you look at it and believe he's making an unbelievable throw to get someone out

If you're not, you know that Tatis is forking up the throw :)

## Development Setup

### Using Docker (Recommended)

The easiest way to get started is using Docker Compose:

1. Clone the repository
2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
3. Start the services:
   ```bash
   docker-compose up
   ```
4. The application will be available at http://localhost:8000

The Docker setup includes:
- Django development server with live code reloading
- PostgreSQL 16 database
- Automatic database migrations on startup
- Volume mounts for persistent data

To stop the services:
```bash
docker-compose down
```

To rebuild after dependency changes:
```bash
docker-compose up --build
```

### Traditional Setup (Without Docker)

If you prefer not to use Docker:

1. Install Python 3.13+
2. Install dependencies:
   ```bash
   uv pip install -e .
   ```
3. Set up environment variables (create a `.env` file or export them)
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Production Deployment

### Deploying to Coolify

This application is ready for deployment to Coolify:

1. In Coolify, create a new application from this Git repository
2. Set the following environment variables:
   - `DATABASE_URL`: PostgreSQL connection string
   - `SECRET_KEY`: Django secret key (generate a secure one)
   - `DEBUG=False`
   - `ALLOWED_HOSTS`: Your domain name(s)
   - `SECURE_SSL_REDIRECT=True`
   - `SESSION_COOKIE_SECURE=True`
   - `CSRF_COOKIE_SECURE=True`
   - `SECURE_HSTS_SECONDS=31536000`
   - `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`
   - `SECURE_HSTS_PRELOAD=True`
   - `SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https`
3. Coolify will automatically build and deploy using the Dockerfile

The application includes:
- Health check endpoint at `/health/` for Coolify monitoring
- Automatic database migrations on container startup
- Static file collection during build
- Gunicorn as the production WSGI server

## Development Commands

### Testing
```bash
pytest                    # Run all tests
pytest --cov              # Run with coverage
pytest --last-failed      # Run only failed tests
```

### Code Quality
```bash
prek run --all-files     # Run pre-commit hooks
ruff format .            # Format code
ruff check --fix .       # Lint and fix
djhtml .                 # Format Django templates
ty                       # Type checking
```

### Database
```bash
python manage.py migrate              # Run migrations
python manage.py makemigrations       # Create migrations
python manage.py loaddata fixture/*.json  # Load fixtures (if exist)
```
