from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    is_locked = models.BooleanField(default=False)
    guest_can_pause = models.BooleanField(default=False)
    votes_to_skip = models.PositiveSmallIntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.host.username} - {self.code}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)