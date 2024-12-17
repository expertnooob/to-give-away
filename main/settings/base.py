from pathlib import Path
import environ

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize the environment variables
env = environ.Env()
environ.Env.read_env()

# Secret key for the application (should be different in production)
SECRET_KEY = env('SECRET_KEY')

# Debug mode, should be True in development and False in production
DEBUG = True

# Hosts allowed to serve your app
ALLOWED_HOSTS = []

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# apps that you create for your project
DJANGO_APPS = [
    'apps.togiveaway',
    'apps.user',
    'drf_yasg',
]

# third-party apps that are installed via pip
THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

INSTALLED_APPS = DEFAULT_APPS + DJANGO_APPS + THIRD_PARTY_APPS

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'main.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# WSGI application entry point
WSGI_APPLICATION = 'main.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# Define a custom security scheme
SECURITY_SCHEMES = {
    "Token": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header",
        "description": "Enter your token in the format: Token <your_token>",
    }
}

# Add the security definition to the schema
swagger_security_definitions = {
    "default": [
        {
            "Authorization": {"type": "Token"},
        }
    ]
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = 'user.CustomUser'

# Static files
STATIC_URL = 'static/'

# Default auto field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
