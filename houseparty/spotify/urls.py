from django.urls import path
from .views import AuthURL, SpotifyCallback, SpotifyRefreshToken, SpotifyDevices, PlayerAPIView


urlpatterns = [

    path('auth-url/', AuthURL.as_view()),
    path('callback/', SpotifyCallback.as_view()),
    path('refresh-token/', SpotifyRefreshToken.as_view()),
    path('player/', PlayerAPIView.as_view(), name='player'),
    path('device/', SpotifyDevices.as_view(), name='device'),
    
]
