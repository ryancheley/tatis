# Build stage - Install dependencies
FROM python:3.14-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install uv for faster dependency installation
RUN pip install --upgrade pip uv

# Set work directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./

# Install Python dependencies
RUN uv pip install --no-cache-dir ".[dev]"

# Runtime stage
FROM python:3.14-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=tatisjr.settings \
    PATH="/opt/venv/bin:$PATH"

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 django && \
    mkdir -p /app /app/staticfiles /app/media && \
    chown -R django:django /app

# Set work directory
WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy project files
COPY --chown=django:django . .

# Copy entrypoint script
COPY --chown=django:django docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Switch to non-root user
USER django

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Set entrypoint
ENTRYPOINT ["docker-entrypoint.sh"]

# Default command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "60", "tatisjr.wsgi:application"]
