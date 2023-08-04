# Generated by Django 4.2.3 on 2023-08-04 12:47

import charityapp.user_profiles.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='volunteer_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Last name')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('DO_NOT_SHOW', 'Do not show')], default=charityapp.user_profiles.models.Gender['DO_NOT_SHOW'], max_length=30, verbose_name='Gender')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('phone_number', models.CharField(blank=True, null=True, verbose_name='Phone number')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='About')),
                ('interests', models.CharField(choices=[('ENVIRONMENTAL_CAUSES', 'Environmental causes'), ('HUMANITARIAN_CAUSES', 'Humanitarian causes'), ('DISASTERS_AND_ACCIDENTS_CAUSES', 'Causes of disasters and accidents'), ('ANIMAL_CAUSES', 'Animal causes'), ('OTHER', 'Other')], max_length=30, verbose_name='Charity interests')),
                ('charity_history', models.ManyToManyField(to='work.charitycampaigns', verbose_name='Charity history')),
                ('donation_history', models.ManyToManyField(to='work.donationcampaigns', verbose_name='Donation history')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='sponsor_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(max_length=100, verbose_name='Company name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('website', models.URLField(verbose_name='Website')),
                ('career_field', models.CharField(blank=True, max_length=100, null=True, verbose_name='Career field')),
                ('donation_history', models.ManyToManyField(to='work.donationcampaigns', verbose_name='Donation history')),
            ],
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='member_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Last name')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('DO_NOT_SHOW', 'Do not show')], default=charityapp.user_profiles.models.Gender['DO_NOT_SHOW'], max_length=30, verbose_name='Gender')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('phone_number', models.CharField(blank=True, null=True, verbose_name='Phone number')),
                ('strengths', models.TextField(blank=True, null=True, verbose_name='Strengths')),
                ('interests', models.CharField(choices=[('ENVIRONMENTAL_CAUSES', 'Environmental causes'), ('HUMANITARIAN_CAUSES', 'Humanitarian causes'), ('DISASTERS_AND_ACCIDENTS_CAUSES', 'Causes of disasters and accidents'), ('ANIMAL_CAUSES', 'Animal causes'), ('OTHER', 'Other')], max_length=30, verbose_name='Charity interests')),
                ('role', models.CharField(choices=[('CHAIRMAN', 'Chairman'), ('VICE_CHAIRMAN', 'Vice Chairman'), ('SECRETARY', 'Secretary'), ('ADMINISTRATOR', 'Administrator'), ('MODERATOR', 'Moderator'), ('CASHIER', 'Cashier'), ('PR', 'Public Relations (PR)'), ('OTHER', 'Other')], max_length=13, verbose_name='Role in the club')),
                ('charity_history', models.ManyToManyField(to='work.charitycampaigns', verbose_name='Charity history')),
            ],
        ),
    ]
