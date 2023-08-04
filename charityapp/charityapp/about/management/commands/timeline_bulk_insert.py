from django.core.management.base import BaseCommand

from charityapp.about.models import Timeline


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        timeline_data = [
            {
                'event_date': '2017-10-28',
                'event_title': 'The beginning',
                'event_summary': 'The first campaign was announced on October 28, 2017 on the page of the sports club and was seen by over 400,000 people, and on the day itself in 3 hours 8 and a half tons of caps were collected.',
                'event_image': None,
            },
            {
                'event_date': '2017-04-14',
                'event_title': 'The campaign outside the borders of Sofia',
                'event_summary': 'With the second campaign announced for Sofia, the city of Plovdiv also announcesthat they are doing such a campaign, so gradually in every corner of Bulgaria people start collecting caps.We do it because we believe that Bulgaria and the world as a whole can become a more pleasant place to live when each of us starts making daily efforts to do so.',
                'event_image': None,
            },
            {
                'event_date': '2017-07-20',
                'event_title': 'First Donation',
                'event_summary': 'The funds collected from the "Caps for the Future" campaign were used to purchase the first incubators for newborns in hospitals. This opened up new opportunities for early medical care for the most vulnerable little patients, saving lives.',
                'event_image': None,
            },
            {
                'event_date': '2018-10-20',
                'event_title': 'Second Donation',
                'event_summary': 'We were able to purchase the SECOND incubator thanks to the TONS of caps we collected and recycled TOGETHER! The incubator thank was donated to Chirpan`s Hospital',
                'event_image': None,
            },
            {
                'event_date': '2018-11-26',
                'event_title': 'Third Donation',
                'event_summary': 'We were able to purchase the THIRD incubator thanks to the TONS of caps we collected and recycled TOGETHER! The incubator thank was donated to Botevgrad`s Hospital',
                'event_image': None,
            },
            {
                'event_date': '2019-02-28',
                'event_title': 'Expansion of Campaigns',
                'event_summary': 'Thanks to the commitment and support of the community, the "Caps for the Future" campaign gained popularity and expanded. New ideas and projects emerged, including the collection of other recyclable materials to support various needs.',
                'event_image': None,
            },
            {
                'event_date': '2019-05-22',
                'event_title': 'National Projects and Programs',
                'event_summary': 'The "Caps for the Future" organization became a partner in national projects and programs focused on environmental conservation and sustainability. Working alongside various organizations, governmental and private institutions, we actively contribute to the fight against pollution and the preservation of natural resources.',
                'event_image': None,
            },
            {
                'event_date': '2020-10-01',
                'event_title': 'First Neonatal Ambulances',
                'event_summary': 'With the funds raised from recent campaigns, we purchased specialized neonatal ambulances, providing swift and safe transportation for newborns to the hospital. The new ambulances increase the chances of early detection and treatment of high-risk pregnancies, saving the lives of the little ones.',
                'event_image': None,
            },
            {
                'event_date': '2021-03-01',
                'event_title': 'Aluminum cans',
                'event_summary': 'The beginning of the collection of aluminum cans (separate from the caps).',
                'event_image': None,
            },
            {
                'event_date': '2021-05-01',
                'event_title': 'Many Donations',
                'event_summary': 'The funds collected from the "Caps for the Future" campaign were used to purchase the first incubators for newborns in hospitals. This opened up new opportunities for early medical care for the most vulnerable little patients, saving lives.',
                'event_image': None,
            },
            {
                'event_date': '2022-11-18',
                'event_title': 'The beginning of "Clubs for Future"',
                'event_summary': 'The "Caps for the Future" program expanded with the establishment of volunteer clubs in different cities. These clubs unite people with common goals and stimulate volunteer efforts to support children and families in need.',
                'event_image': None,
            },
            {
                'event_date': '2023-01-14',
                'event_title': 'New Projects and Initiatives',
                'event_summary': 'We continue to create new projects and initiatives focused on supporting healthcare, education, and social development for children. Our compassion and unwavering commitment to change lead to exciting new opportunities for assistance and support.',
                'event_image': None,
            },
        ]

        instances = [Timeline(**data) for data in timeline_data]
        Timeline.objects.bulk_create(instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in table about_timeline.'))
