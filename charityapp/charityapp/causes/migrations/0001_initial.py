# Generated by Django 4.2.3 on 2023-08-09 14:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharityCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('resume', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('motivation', models.TextField()),
                ('type', models.CharField(choices=[('ENVIRONMENTAL_CHARITY', 'Environmental Charity'), ('CHILDRENS_CHARITY', 'Children’s Charity'), ('HUMAN_RIGHTS_CHARITY', 'Human Rights Charity'), ('DISASTER_RELIEF_CHARITY', 'Disaster Relief Charity'), ('SCIENTIFIC_RESEARCH_CHARITY', 'Scientific Research Charity'), ('SENIOR_CITIZEN_CHARITY', 'Senior Citizen Charity'), ('CULTURAL_CHARITY', 'Cultural Charity'), ('ANIMAL_BASED_CHARITY', 'Animal-Based Charity'), ('SPORTS_BASED_CHARITY', 'Sports-Based Charity'), ('EDUCATION_CHARITY', 'Education Charity'), ('OTHER', 'Other')], max_length=27)),
                ('website', models.URLField(blank=True, null=True)),
                ('start_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('place', models.CharField(blank=True, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Charity Campaign',
                'verbose_name_plural': 'Charity Campaigns',
            },
        ),
        migrations.CreateModel(
            name='DonationCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('purpose', models.TextField()),
                ('goal_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('current_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('succeeded', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Donation Campaign',
                'verbose_name_plural': 'Donation Campaigns',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('important', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='SponsorDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donation_date', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='causes.donationcampaign')),
            ],
        ),
    ]
