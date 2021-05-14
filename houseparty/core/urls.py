from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ControlCenterAPIView

router = DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')

urlpatterns = [
    path('', include(router.urls)),
    path('control-center/', ControlCenterAPIView.as_view(), name='control-center'),
]
