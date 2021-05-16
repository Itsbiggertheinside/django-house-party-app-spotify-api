from django.urls import re_path
from .consumers import WebSocketConsumer


websocket_urlpatterns = [

    re_path(r'ws/room/(?P<room_code>[^/]+)/$', WebSocketConsumer.as_asgi()),
    
]