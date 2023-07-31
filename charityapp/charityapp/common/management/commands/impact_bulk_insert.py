from django.core.management import BaseCommand

from charityapp.common.models import Impact


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        impact_data = [
            {
                'title': 'Supporters',
                'resume': 'Charity supporters have a profound impact on the success of our charitable endeavors.'
                          ' Their participation fosters a sense of community and compassion, inspiring others to join the effort to create together a better world for all.'
                          ' We are meeting more and more like-minded people!',
                'picture': 'static/images/Supporters.png',
                'achievement_numbers': 130000,
            },
            {
                'title': 'Sponsors',
                'resume': 'Our sponsors play a vital role in helping us fulfill our missions and make a positive impact on a variety of social, environmental and humanitarian issues. '
                          'With your participation, you help us bridge the gap between charitable activities and the resources it needs to achieve its goals. ',
                'picture': 'static/images/Sponsors.png',
                'achievement_numbers': 1500,
            },
            {
                'title': 'Campaigns',
                'resume': 'Our efforts are aimed at addressing various social, environmental, and humanitarian issues. Our campaigns rely on people\'s compassion and generosity to improve the country\'s living environment. '
                          'They play a vital role in tackling pressing issues and creating positive change in society.',
                'picture': 'static/images/Campaigns.png',
                'achievement_numbers': 25,
            },
            {
                'title': 'Donations',
                'resume': 'The donations we make play a crucial role in solving societal problems, promoting positive change and supporting various humanitarian and social causes.'
                          ' These are material donations based on donations to the foundation and the funds raised from all our campaigns.',
                'picture': 'static/images/Donated.png',
                'achievement_numbers': 580,
            },
            {
                'title': 'Donated',
                'resume': 'The donations we make play a crucial role in solving societal problems, promoting positive change and supporting various humanitarian and social causes.'
                          ' This is the amount equivalent to the donations made',
                'picture': 'static/images/Donations.png',
                'achievement_numbers': 150560,
            },
            {
                'title': 'Members',
                'resume': 'We collectively work together to advance the foundation\'s mission, address societal needs, and make a positive impact on the lives of those they aim to help. '
                          'Together we are more powerful, we can do more...',
                'picture': 'static/images/Members.png',
                'achievement_numbers': 1200,
            },

        ]

        # Create instances from the data and bulk insert into the database
        instances = [Impact(**data) for data in impact_data]
        Impact.objects.bulk_create(instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in table common_impact.'))
