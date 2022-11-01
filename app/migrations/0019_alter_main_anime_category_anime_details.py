# Generated by Django 4.0.5 on 2022-07-04 03:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_main_anime_trailer_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('A', 'action'), ('SC', 'scifi'), ('RC', 'romcom')], max_length=2),
        ),
        migrations.CreateModel(
            name='anime_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_name_details', models.CharField(max_length=100)),
                ('description_details', models.CharField(blank=True, max_length=100)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1, 0), django.core.validators.MaxValueValidator(5, 0)])),
                ('img_details', models.ImageField(upload_to='animeimg')),
                ('genre_details', models.CharField(max_length=100)),
                ('anime_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='app.main_anime')),
            ],
        ),
    ]