# Generated by Django 4.2.1 on 2023-05-07 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0006_alter_session_loggedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='loggedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 7, 17, 8, 46, 753634)),
        ),
    ]
