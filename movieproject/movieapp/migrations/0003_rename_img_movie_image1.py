# Generated by Django 3.2.7 on 2021-09-17 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='image1',
        ),
    ]
