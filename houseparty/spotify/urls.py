from django.urls import path
from .views import AuthURL, SpotifyCallback, SpotifyRefreshToken


urlpatterns = [

    path('auth-url/', AuthURL.as_view()),
    path('callback/', SpotifyCallback.as_view()),
    path('refresh-token/', SpotifyRefreshToken.as_view()),
    
]
