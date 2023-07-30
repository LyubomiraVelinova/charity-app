# Generated by Django 4.2.3 on 2023-07-28 11:24

import charityapp.user_profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
        ('user_profiles', '0006_alter_memberprofile_contribution_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='contribution_history',
            field=models.ManyToManyField(to='work.charitycampaigns', verbose_name='MY CONTRIBUTION HISTORY'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('DO_NOT_SHOW', 'Do not show')], default=charityapp.user_profiles.models.Gender['DO_NOT_SHOW'], max_length=30, verbose_name='MY GENDER'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='interests',
            field=models.CharField(choices=[('ENVIRONMENTAL_CAUSES', 'Environmental causes'), ('HUMANITARIAN_CAUSES', 'Humanitarian causes'), ('DISASTERS_AND_ACCIDENTS_CAUSES', 'Causes of disasters and accidents'), ('ANIMAL_CAUSES', 'Animal causes'), ('OTHER', 'Other')], max_length=30, verbose_name='MY INTERESTS'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='phone_number',
            field=models.CharField(blank=True, null=True, verbose_name='MY PHONE NUMBER'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='role',
            field=models.CharField(choices=[('CHAIRMAN', 'Chairman'), ('VICE_CHAIRMAN', 'Vice Chairman'), ('SECRETARY', 'Secretary'), ('ADMINISTRATOR', 'Administrator'), ('MODERATOR', 'Moderator'), ('CASHIER', 'Cashier'), ('PR', 'Public Relations (PR)'), ('OTHER', 'Other')], max_length=13, verbose_name='MY ROLE IN THE CLUB'),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='strengths',
            field=models.TextField(blank=True, null=True, verbose_name='MY SUPER POWER'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='career_field',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='OUR CAREER FIELD'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='donation_history',
            field=models.ManyToManyField(to='work.donationcampaigns', verbose_name='OUR DONATION HISTORY'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='website',
            field=models.URLField(verbose_name='OUR WEBSITE'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='MY BIOGRAPHY'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='charity_history',
            field=models.ManyToManyField(to='work.charitycampaigns', verbose_name='MY CHARITY HISTORY'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='donation_history',
            field=models.ManyToManyField(to='work.donationcampaigns', verbose_name='MY DONATION HISTORY'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('DO_NOT_SHOW', 'Do not show')], default=charityapp.user_profiles.models.Gender['DO_NOT_SHOW'], max_length=30, verbose_name='MY GANDER'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='interests',
            field=models.TextField(verbose_name='MY CHARITY INTERESTS'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='phone_number',
            field=models.CharField(blank=True, null=True, verbose_name='MY PHONE NUMBER'),
        ),
    ]