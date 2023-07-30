# Generated by Django 4.2.3 on 2023-07-29 15:07

import charityapp.user_profiles.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
        ('user_profiles', '0012_alter_volunteerprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='charity_history',
            field=models.ManyToManyField(to='work.charitycampaigns', verbose_name='Charity history'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('DO_NOT_SHOW', 'Do not show')], default=charityapp.user_profiles.models.Gender['DO_NOT_SHOW'], max_length=30, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='interests',
            field=models.CharField(choices=[('ENVIRONMENTAL_CAUSES', 'Environmental causes'), ('HUMANITARIAN_CAUSES', 'Humanitarian causes'), ('DISASTERS_AND_ACCIDENTS_CAUSES', 'Causes of disasters and accidents'), ('ANIMAL_CAUSES', 'Animal causes'), ('OTHER', 'Other')], max_length=30, verbose_name='Charity interests'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='phone_number',
            field=models.CharField(blank=True, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='role',
            field=models.CharField(choices=[('CHAIRMAN', 'Chairman'), ('VICE_CHAIRMAN', 'Vice Chairman'), ('SECRETARY', 'Secretary'), ('ADMINISTRATOR', 'Administrator'), ('MODERATOR', 'Moderator'), ('CASHIER', 'Cashier'), ('PR', 'Public Relations (PR)'), ('OTHER', 'Other')], max_length=13, verbose_name='Role in the club'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='strengths',
            field=models.TextField(blank=True, null=True, verbose_name='Strengths'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='career_field',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Career field'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='Company name'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='donation_history',
            field=models.ManyToManyField(to='work.donationcampaigns', verbose_name='Donation history'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='website',
            field=models.URLField(verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='charity_history',
            field=models.ManyToManyField(to='work.charitycampaigns', verbose_name='Charity history'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='donation_history',
            field=models.ManyToManyField(to='work.donationcampaigns', verbose_name='Donation history'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('DO_NOT_SHOW', 'Do not show')], default=charityapp.user_profiles.models.Gender['DO_NOT_SHOW'], max_length=30, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='interests',
            field=models.CharField(choices=[('ENVIRONMENTAL_CAUSES', 'Environmental causes'), ('HUMANITARIAN_CAUSES', 'Humanitarian causes'), ('DISASTERS_AND_ACCIDENTS_CAUSES', 'Causes of disasters and accidents'), ('ANIMAL_CAUSES', 'Animal causes'), ('OTHER', 'Other')], max_length=30, verbose_name='Charity interests'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='phone_number',
            field=models.CharField(blank=True, null=True, verbose_name='Phone number'),
        ),
    ]