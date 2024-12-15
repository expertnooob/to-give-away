import os
from django.core.wsgi import get_wsgi_application

# Check the environment and set the settings module dynamically
environment = os.environ.get('DJANGO_ENV', 'local')  # Default to 'local' if not set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'main.settings.{environment}')

application = get_wsgi_application()
