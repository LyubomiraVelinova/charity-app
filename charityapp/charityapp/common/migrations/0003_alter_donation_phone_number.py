# Generated by Django 4.2.3 on 2023-08-10 17:18

import charityapp.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_rename_randomuserdonation_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[charityapp.common.validators.validate_phone]),
        ),
    ]
