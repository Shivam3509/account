# Generated by Django 4.1.2 on 2022-10-10 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_customuser_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
    ]
