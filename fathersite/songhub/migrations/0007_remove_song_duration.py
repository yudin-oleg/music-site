# Generated by Django 3.2.4 on 2021-06-14 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songhub', '0006_song_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
    ]
