# Generated by Django 4.2.3 on 2023-08-10 16:40

import charityapp.user_profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='phone_number',
            field=models.CharField(default='0888778999', max_length=13, validators=[charityapp.user_profiles.validators.validate_phone], verbose_name='Phone number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='phone_number',
            field=models.CharField(default='0888778999', max_length=13, validators=[charityapp.user_profiles.validators.validate_phone], verbose_name='Phone number'),
            preserve_default=False,
        ),
    ]
