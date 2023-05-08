# Generated by Django 4.2.1 on 2023-05-07 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0007_alter_session_loggedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='refresh_token',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='loggedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 7, 18, 17, 13, 7324)),
        ),
    ]