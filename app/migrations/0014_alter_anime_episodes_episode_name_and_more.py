# Generated by Django 4.0.2 on 2022-06-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_anime_episodes_episode_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime_episodes',
            name='episode_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='anime_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('A', 'action'), ('RC', 'romcom'), ('SC', 'scifi')], max_length=2),
        ),
    ]
