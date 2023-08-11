from django.core.management.base import BaseCommand

from charityapp.user_accounts.models import AppUser
from charityapp.user_profiles.models import Testimonial


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        testimonials_data = [
            {
                'quote': 'I am truly grateful for being part of this amazing charity organization. The work they do to support those in need is inspiring and impactful. As a member, I have had the opportunity to contribute to various initiatives that make a real difference in people`s lives. The sense of community and camaraderie among the members is heartwarming. It`s an honor to be associated with such a dedicated team of volunteers and sponsors who are committed to making the world a better place. I encourage everyone to join this noble cause and be a part of the positive change we create together.',
                'approved': 'True',
                'author': AppUser.objects.get(email='member1@ex.com'),
            },
            {
                'quote': 'I may not be able to volunteer on-site or contribute large donations, but I believe in the mission of this charity wholeheartedly. I show my support by sharing their messages on social media and attending their events whenever possible. Every small action counts, and I`m proud to be part of their journey.',
                'approved': 'True',
                'author': AppUser.objects.get(email='volunteer1@ex.com'),
            },
            {
                'quote': 'As a company, we value social responsibility and giving back to the community. Partnering with this charity organization has been a fantastic experience. Their professionalism, transparency, and dedication to their cause make them an ideal partner for us. We`re proud to be associated with an organization that truly makes a difference.',
                'approved': 'True',
                'author': AppUser.objects.get(email='sponsor1@ex.com'),
            },
            {
                'quote': 'Becoming a member of this charity organization has been a wonderful decision. I`ve had the chance to collaborate with like-minded individuals who are passionate about making a difference. Together, we`ve organized successful fundraisers and community outreach programs that have had a positive impact on many lives.',
                'approved': 'True',
                'author': AppUser.objects.get(email='volunteer2@ex.com'),
            },
            {
                'quote': 'I`ve been supporting this charity organization for several years now, and I`m continually impressed by the impact they make in the community. Knowing that my donations contribute to meaningful projects and initiatives gives me a sense of fulfillment and purpose. I wholeheartedly believe in their mission and will continue to support their efforts.',
                'approved': 'True',
                'author': AppUser.objects.get(email='member2@ex.com'),
            },
            {
                'quote': 'I cannot express enough gratitude for the support I`ve received from this charity. They provided me with much-needed assistance during a difficult time in my life, and their kindness and generosity helped me get back on my feet. They truly care about the well-being of others, and I will forever be thankful for their help.',
                'approved': 'True',
                'author': AppUser.objects.get(email='sponsor2@ex.com'),
            },
            {
                'quote': 'Volunteering with this charity organization has been an incredibly rewarding experience. I`ve had the opportunity to make a meaningful impact on the lives of those in need, and it has also enriched my own life in ways I couldn`t have imagined. The team here is dedicated and inspiring, and I`m proud to be a part of such a compassionate community.',
                'approved': 'True',
                'author': AppUser.objects.get(email='volunteer3@ex.com'),
            },
        ]

        instances = [Testimonial(**data) for data in testimonials_data]
        Testimonial.objects.bulk_create(instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in user_profiles_testimonials table.'))
