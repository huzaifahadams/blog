# Generated by Django 4.0 on 2021-12-13 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adams_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
