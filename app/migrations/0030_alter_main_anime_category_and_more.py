# Generated by Django 4.0.5 on 2022-07-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_feedback_feedbck_alter_main_anime_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('TR', 'TopRated'), ('N', 'Newest'), ('AB', 'AllTimeBest')], max_length=2),
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='description',
            field=models.TextField(),
        ),
    ]
