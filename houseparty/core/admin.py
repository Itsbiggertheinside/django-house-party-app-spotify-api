from django.contrib import admin
from .models import Room, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Room)