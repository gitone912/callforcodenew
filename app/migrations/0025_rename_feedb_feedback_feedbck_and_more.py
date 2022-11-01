# Generated by Django 4.0.5 on 2022-07-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_feedback_alter_main_anime_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedb',
            new_name='feedbck',
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('AB', 'AllTimeBest'), ('TR', 'TopRated'), ('N', 'Newest')], max_length=2),
        ),
    ]
