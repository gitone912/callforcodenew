# Generated by Django 4.0.5 on 2022-07-03 11:50

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_main_anime_anime_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_anime',
            name='trailer_link',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]
