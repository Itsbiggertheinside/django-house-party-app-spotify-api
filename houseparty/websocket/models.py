from django.db import models


# Create your models here.
class Player(models.Model):
    room = models.OneToOneField('core.Room', on_delete=models.CASCADE)
    current_song = models.CharField(max_length=255, default='')
    skip_votes = models.ManyToManyField('core.Profile')

    def __str__(self):
        return 'Room Player'