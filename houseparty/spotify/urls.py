from django.urls import path
from .views import AuthURL, SpotifyCallback, SpotifyRefreshToken, ControlCenterAPIView, PlayerAPIView


urlpatterns = [

    path('auth-url/', AuthURL.as_view()),
    path('callback/', SpotifyCallback.as_view()),
    path('refresh-token/', SpotifyRefreshToken.as_view()),
    path('control-center/', ControlCenterAPIView.as_view(), name='control-center'),
    path('player/', PlayerAPIView.as_view(), name='player'),
    
]
