# Generated by Django 4.2.3 on 2023-08-09 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('member_role', models.CharField(max_length=100)),
                ('profile_picture', models.URLField(default='static/images/anonymous_profile.jpg')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Our People',
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('event_title', models.CharField(max_length=100)),
                ('event_summary', models.TextField()),
                ('event_image', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Timeline Data',
                'verbose_name_plural': 'Timeline Data',
            },
        ),
    ]
