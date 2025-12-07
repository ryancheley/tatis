#!/bin/bash
set -e

# Wait for database to be ready
echo "Waiting for database..."
while ! python -c "
import os
import sys
import psycopg
from urllib.parse import urlparse

try:
    db_url = os.environ.get('DATABASE_URL', '')
    if db_url:
        parsed = urlparse(db_url)
        conn = psycopg.connect(
            host=parsed.hostname,
            port=parsed.port or 5432,
            dbname=parsed.path.lstrip('/'),
            user=parsed.username,
            password=parsed.password,
            connect_timeout=3
        )
        conn.close()
        sys.exit(0)
    else:
        print('DATABASE_URL not set')
        sys.exit(1)
except Exception as e:
    print(f'Database connection failed: {e}')
    sys.exit(1)
" 2>/dev/null; do
    echo "Database unavailable - waiting..."
    sleep 2
done

echo "Database is ready!"

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Load fixtures if they exist (optional)
if [ -d "fixture" ] && [ "$(ls -A fixture/*.json 2>/dev/null)" ]; then
    echo "Loading fixtures..."
    python manage.py loaddata fixture/*.json || echo "No fixtures to load or loading failed"
fi

echo "Starting application..."
exec "$@"
