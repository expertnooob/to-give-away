from .base import *

# Local development specific settings

# Use SQLite for development
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

# Enable debugging in local environment
DEBUG = True

# Allow local hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']