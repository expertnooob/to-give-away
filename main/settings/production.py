from .base import *

# Production specific settings

DEBUG = False

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'your_production_db',
    'USER': 'your_production_user',
    'PASSWORD': 'your_production_password',
    'HOST': 'your_production_db_host',
    'PORT': '5432',
}

# Add your production allowed hosts
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Secure cookies and other production-related settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True