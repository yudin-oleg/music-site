# Generated by Django 3.2.4 on 2021-06-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songhub', '0003_alter_song_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.CharField(max_length=15),
        ),
    ]
