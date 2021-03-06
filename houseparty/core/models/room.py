from django.db import models
from .profile import Profile


class Room(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    host = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_locked = models.BooleanField(default=False)
    guest_can_pause = models.BooleanField(default=False)
    votes_to_skip = models.PositiveSmallIntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.host} - {self.code}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)