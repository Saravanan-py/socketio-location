"""
WSGI config for kafka_project1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import socketio
from socketio import Middleware,ASGIApp,WSGIApp
from kafka_app.views import sio
from django.core.wsgi import get_wsgi_application
import eventlet.wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kafka_project1.settings')
app = get_wsgi_application()
application = Middleware(sio, app)
eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8000)), application)


# import os
# import socketio
# from socketio import WSGIApp
# from kafka_app.views import sio
# from django.core.wsgi import get_wsgi_application
# import eventlet.wsgi
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kafka_project1.settings')
# application = get_wsgi_application()
# application = WSGIApp(sio, application)
# eventlet.wsgi.server(eventlet.listen(('', 8000)), application)
