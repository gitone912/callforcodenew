# Generated by Django 4.0.2 on 2022-06-23 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='main_anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('A', 'action'), ('RC', 'romcom'), ('SC', 'scifi')], max_length=2)),
                ('episode_thumbnail', models.ImageField(upload_to='animeimg')),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('added', models.DateTimeField(auto_now=True)),
                ('link', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_names', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.main_anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('anime_watched', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='anime_episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_name', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display', to='app.main_anime')),
            ],
        ),
    ]