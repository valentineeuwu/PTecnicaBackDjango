# Generated by Django 4.2.1 on 2023-05-08 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0012_alter_session_loggedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='loggedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 7, 20, 36, 26, 548975)),
        ),
    ]
