# This file contains the WSGI configuration required to serve up your
# Django app
import os
import sys
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application
# Add your project directory to the sys.path
settings_path = (os.getenv('PATH_TO_SETTINGS_FILE'))
sys.path.insert(0, settings_path)
load_dotenv(os.getenv('PATH_TO_ENV_FILE'))

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'where_to_go.settings'

# Set the 'application' variable to the Django wsgi app

application = get_wsgi_application()
