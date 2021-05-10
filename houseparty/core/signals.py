from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Room
from websocket.models import Player, Listener


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Room)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(room=instance)
        Listener.objects.create(room=instance)