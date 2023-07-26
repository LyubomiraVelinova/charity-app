from django.core.management.base import BaseCommand

from charityapp.work.models import DonationCampaigns, CharityCampaigns


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        donation_data = [
            DonationCampaigns(title='Donation', description='This is a donation campaign', goal_amount=3400.00,
                              motivation='Lets work!', start_date='2023-05-23', end_date='2023-07-17',
                              current_amount=1800.00),
            DonationCampaigns(title='Donation3', description='This is a donation3 campaign', goal_amount=1800.00,
                              motivation='Lets work!', start_date='2023-05-23', end_date='2023-07-17',
                              current_amount=1800.00, succeeded=True),
        ]

        charity_data = [
            CharityCampaigns(name='True', resume='True', image='https.jsxj.com', description='jsbj',
                             motivation='jsjnjs', type='Environmental Charity"')
        ]

        # HAVEN`T TRIED IT

        # unique_field_values = set(CharityCampaigns.objects.values_list('unique_field', flat=True))
        # new_data_to_insert = [data for data in charity_data if data['unique_field'] not in unique_field_values]
        # CharityCampaigns.objects.bulk_create([CharityCampaigns(**data) for data in new_data_to_insert])

        DonationCampaigns.objects.bulk_create(donation_data)
        CharityCampaigns.objects.bulk_create(charity_data)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
