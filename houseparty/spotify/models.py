from django.db import models


# Create your models here.
class SpotifyToken(models.Model):
    profile = models.OneToOneField('core.Profile', on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    token_type = models.CharField(max_length=75, null=True, blank=True)
    expires_in = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Spotify Token'