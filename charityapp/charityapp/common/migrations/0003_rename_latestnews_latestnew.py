# Generated by Django 4.2.3 on 2023-08-05 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_aboutusinfo_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LatestNews',
            new_name='LatestNew',
        ),
    ]