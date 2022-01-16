from django.conf.urls import url
from channels.routing import URLRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from authapi import views
import django_eventstream
from django_eventstream import send_event

urlpatterns = [
    url(r'^stream/', AuthMiddlewareStack(
        URLRouter(django_eventstream.routing.urlpatterns)
    ), {'channels': ['test']}),
    url(r'', AsgiHandler),
]