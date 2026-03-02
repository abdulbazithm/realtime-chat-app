import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import django

django.setup()   

import mychat.routing  

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            mychat.routing.websocket_urlpatterns
        )
    ),
})