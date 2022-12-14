# Generated by Django 4.0.2 on 2022-06-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_main_anime_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('SC', 'scifi'), ('RC', 'romcom'), ('A', 'action')], max_length=2),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='description',
            field=models.TextField(max_length=130),
        ),
    ]
