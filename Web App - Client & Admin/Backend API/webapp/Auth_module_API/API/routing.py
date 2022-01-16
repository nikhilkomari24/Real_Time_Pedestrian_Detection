from channels.routing import ProtocolTypeRouter, URLRouter
from authapi import routing

application = ProtocolTypeRouter({
    'http': URLRouter(routing.urlpatterns),
})