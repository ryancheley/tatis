from pathlib import Path

import environ

env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    DATABASE_URL=(str, "psql://postgres:postgres@127.0.0.1:5432/github_actions"),
    SECRET_KEY=(str, "33p=mm5j9@ptu1mopm2gd-o4xjs#(n_75b_x(-5r0#6espl2&d"),
    SECURE_HSTS_INCLUDE_SUBDOMAINS=(bool, False),
    SECURE_HSTS_PRELOAD=(bool, False),
    SECURE_HSTS_SECONDS=(int, 0),
    SECURE_SSL_REDIRECT=(bool, False),
    SESSION_COOKIE_SECURE=(bool, False),
    CSRF_COOKIE_SECURE=(bool, False),
    SECURE_PROXY_SSL_HEADER=(str, None),
)

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")


ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[
        "testserver",
        "127.0.0.1",
    ],
)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "constance",
    "constance.backends.database",
    "django_extensions",
    "health_check",
    "health_check.db",
    # local
    "content",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_permissions_policy.PermissionsPolicyMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tatisjr.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tatisjr.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": env.db()
    | {
        "CONN_MAX_AGE": 0,
        "OPTIONS": {
            "pool": True,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Los_Angeles"

USE_I18N = True


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = Path(BASE_DIR / "static")

# Enable WhiteNoise's compression and caching support
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security Settings Below

SECURE_HSTS_SECONDS = env("SECURE_HSTS_SECONDS")
SECURE_HSTS_INCLUDE_SUBDOMAINS = env("SECURE_HSTS_INCLUDE_SUBDOMAINS")
SECURE_SSL_REDIRECT = env("SECURE_SSL_REDIRECT")
SESSION_COOKIE_SECURE = env("SESSION_COOKIE_SECURE")
CSRF_COOKIE_SECURE = env("CSRF_COOKIE_SECURE")
SECURE_HSTS_PRELOAD = env("SECURE_HSTS_PRELOAD")
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Trust proxy headers from Coolify/Caddy
if secure_proxy := env("SECURE_PROXY_SSL_HEADER", default=None):
    header, value = secure_proxy.split(",")
    SECURE_PROXY_SSL_HEADER = (header, value)

PERMISSIONS_POLICY = {
    "accelerometer": [],
    "ambient-light-sensor": [],
    "autoplay": [],
    "camera": [],
    "document-domain": [],
    "encrypted-media": [],
    "fullscreen": [],
    "geolocation": [],
    "gyroscope": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "usb": [],
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "null": {
            "class": "logging.NullHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
    },
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
}

# Django Constance Configuration
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_CONFIG = {
    "PLAYER_TEAM_ID": (135, "MLB Team ID for the player being tracked (135 = San Diego Padres)", int),
    "PLAYER_LAST_NAME": ("Tatis Jr", "Last name of the player being tracked", str),
    "COLOR_NO_ERROR": ("#FFC425", "Background color when player has no errors (hex color code)", str),
    "COLOR_ERROR": ("#E35625", "Background color when player has an error (hex color code)", str),
    "MESSAGE_ERROR": ("Yes", "Message displayed when player has an error", str),
    "MESSAGE_NO_ERROR": ("Not Yet", "Message displayed when player has no errors", str),
    "MESSAGE_NO_ERROR_INJURED": ("Not Yet *", "Message displayed when player has no errors and is injured", str),
    "IS_INJURED": (False, "Whether the player is currently on the injured list", bool),
    "IS_SUSPENDED": (False, "Whether the player is currently suspended", bool),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "Player Settings": {
        "fields": ("PLAYER_TEAM_ID", "PLAYER_LAST_NAME", "IS_INJURED", "IS_SUSPENDED"),
        "collapse": False,
    },
    "Display Settings": {
        "fields": ("COLOR_NO_ERROR", "COLOR_ERROR"),
        "collapse": False,
    },
    "Message Settings": {
        "fields": ("MESSAGE_ERROR", "MESSAGE_NO_ERROR", "MESSAGE_NO_ERROR_INJURED"),
        "collapse": False,
    },
}
