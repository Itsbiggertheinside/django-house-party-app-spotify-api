# Generated by Django 3.2.2 on 2021-05-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0003_alter_spotifytoken_expires_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='expires_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]