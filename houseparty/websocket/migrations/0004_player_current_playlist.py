# Generated by Django 3.2.2 on 2021-05-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websocket', '0003_listener'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_playlist',
            field=models.CharField(default='', max_length=255),
        ),
    ]
