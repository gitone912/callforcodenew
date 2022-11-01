# Generated by Django 4.0.2 on 2022-06-30 05:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_anime_episodes_episode_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('A', 'action'), ('SC', 'scifi'), ('RC', 'romcom')], max_length=2),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='description',
            field=models.TextField(max_length=130, validators=[django.core.validators.MinValueValidator(129)]),
        ),
    ]