# Generated by Django 4.0.2 on 2022-06-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_main_anime_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='episode_thumbnail',
            field=models.ImageField(height_field='2160px', upload_to='animeimg', width_field='3840px'),
        ),
    ]
