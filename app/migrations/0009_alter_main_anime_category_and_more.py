# Generated by Django 4.0.2 on 2022-06-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_main_anime_episode_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('SC', 'scifi'), ('A', 'action'), ('RC', 'romcom')], max_length=2),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='episode_thumbnail',
            field=models.ImageField(upload_to='animeimg'),
        ),
    ]