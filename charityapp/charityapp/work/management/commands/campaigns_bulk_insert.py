from django.core.management.base import BaseCommand

from charityapp.work.models import DonationCampaigns, CharityCampaigns


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        donation_data = [
            {
                'title': 'Donation',
                'description': 'This is a donation campaign',
                'goal_amount': 3400.00,
                'motivation': 'Lets work!',
                'start_date': '2023-05-23',
                'end_date': '2023-07-17',
                'current_amount': 1800,
            },
        ]

        charity_data = [
            {
                'name': 'Recycling for the Future',
                'resume': 'The number one goal of the campaign is to be good for our environment! Plastic bottles, aluminum and iron jugs and recyclable plastic are collected and with the funds collected separate collection facilities are purchased for the city.',
                'image': 'https.jsxj.com',
                'description': 'jsbj',
                'motivation': 'jsjnjs',
                'type': 'Environmental Charity',
                'website': '',
                'start_date': '',
                'end_date': '',
            },
        ]

        donation_instances = [DonationCampaigns(**data) for data in donation_data]
        charity_instances = [CharityCampaigns(**data) for data in charity_data]
        DonationCampaigns.objects.bulk_create(donation_instances)
        CharityCampaigns.objects.bulk_create(charity_instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))
