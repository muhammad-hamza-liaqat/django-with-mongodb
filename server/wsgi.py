import os

from django.core.wsgi import get_wsgi_application
from server.mongo_util import connect_to_mongo

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
connect_to_mongo()

application = get_wsgi_application()
