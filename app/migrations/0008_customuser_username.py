# Generated by Django 4.1.2 on 2022-10-10 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=datetime.datetime(2022, 10, 10, 7, 54, 38, 478288, tzinfo=datetime.timezone.utc), max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
