from django.urls import path
from .views import WebSocketHandler


urlpatterns = [
    path('real-time/', WebSocketHandler.as_view(), name='websocket-handler')
]
