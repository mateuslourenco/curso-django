# Generated by Django 4.0.1 on 2022-01-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
    ]
