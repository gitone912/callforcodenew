# Generated by Django 4.0.5 on 2022-10-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_homepage_homepage_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('AB', 'AllTimeBest'), ('TR', 'TopRated'), ('N', 'Newest')], max_length=2),
        ),
    ]
