from django.urls import path
from .views import AuthURL, SpotifyCallback


urlpatterns = [

    path('auth-url/', AuthURL.as_view()),
    path('callback/', SpotifyCallback.as_view())
    
]
