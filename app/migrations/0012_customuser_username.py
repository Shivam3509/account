# Generated by Django 4.1.2 on 2022-10-10 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=datetime.datetime(2022, 10, 10, 9, 32, 26, 85557, tzinfo=datetime.timezone.utc), max_length=200, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
    ]
