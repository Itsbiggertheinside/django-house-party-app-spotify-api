from django.db import models


class Room(models.Model):
    code = models.CharField(max_length=14, primary_key=True)
    host = models.ForeignKey('core.Profile', on_delete=models.CASCADE, related_name='rooms')
    is_locked = models.BooleanField(default=False)
    guest_can_pause = models.BooleanField(default=False)
    votes_to_skip = models.PositiveSmallIntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Room {self.code}'