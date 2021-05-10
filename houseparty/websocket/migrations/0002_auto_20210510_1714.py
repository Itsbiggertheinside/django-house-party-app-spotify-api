# Generated by Django 3.2.2 on 2021-05-10 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210506_1750'),
        ('websocket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_song', models.CharField(default='', max_length=255)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.room')),
                ('skip_votes', models.ManyToManyField(to='core.Profile')),
            ],
        ),
        migrations.DeleteModel(
            name='SkipVote',
        ),
    ]