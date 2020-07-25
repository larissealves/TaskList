"""
WSGI config for Tasklist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from Tasklist import MyWSGIApp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tasklist.settings')
application = MyWSGIApp()
application = WhiteNoise(application, root='/path/to/static/files')
application = get_wsgi_application()
