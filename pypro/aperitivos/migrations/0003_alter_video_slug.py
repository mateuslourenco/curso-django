# Generated by Django 4.0.1 on 2022-01-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0002_video_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=32),
        ),
    ]
