# Generated by Django 4.2.1 on 2023-05-08 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
