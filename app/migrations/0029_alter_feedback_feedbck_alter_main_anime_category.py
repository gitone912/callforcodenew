# Generated by Django 4.0.5 on 2022-07-07 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_feedback_feedbck_alter_main_anime_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedbck',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('AB', 'AllTimeBest'), ('N', 'Newest'), ('TR', 'TopRated')], max_length=2),
        ),
    ]