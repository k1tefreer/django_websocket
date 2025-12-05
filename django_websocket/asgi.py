"""
ASGI config for django_websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter

from . import routings  # 导入自己写的websocket主路由

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_websocket.settings")

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # 如果是http请求，则走这里
    "websocket": URLRouter(routings.urlpatterns)  # 如果是websocket则走这里的路由
})


