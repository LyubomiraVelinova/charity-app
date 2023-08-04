# Generated by Django 4.2.3 on 2023-08-04 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharityCampaigns',
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
            ],
        ),
        migrations.CreateModel(
            name='DonationCampaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('motivation', models.TextField()),
                ('goal_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('current_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('succeeded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FAQCampaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('important', models.TextField(blank=True, null=True)),
                ('campaigns', models.ManyToManyField(related_name='q_and_a', to='work.charitycampaigns')),
            ],
        ),
    ]
