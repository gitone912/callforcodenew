# Generated by Django 4.0.2 on 2022-06-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_main_anime_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('RC', 'romcom'), ('A', 'action'), ('SC', 'scifi')], max_length=2),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='description',
            field=models.TextField(max_length=130),
        ),
    ]
