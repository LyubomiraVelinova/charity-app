# Generated by Django 4.2.3 on 2023-08-10 10:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profiles', '0001_initial'),
        ('causes', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CharityCampaign',
            new_name='CharityCause',
        ),
        migrations.RenameModel(
            old_name='DonationCampaign',
            new_name='DonationCause',
        ),
        migrations.RenameModel(
            old_name='SponsorDonation',
            new_name='ParticipationDonationCause',
        ),
    ]
