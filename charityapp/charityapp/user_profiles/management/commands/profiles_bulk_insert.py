from django.core.management.base import BaseCommand

from charityapp.user_accounts.models import AppUser
from charityapp.user_profiles.models import Testimonial, SponsorProfile, VolunteerProfile, MemberProfile


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    #     volunteer_data = [
    #         {
    #             "email": "volunteer1@example.com",
    #             "user_type": "volunteer",
    #             "first_name": "John",
    #             "last_name": "Doe",
    #             "gender": "Male",
    #             "phone_number": "1234567890",
    #             "interests": "Environmental causes",
    #         },
    #         {
    #             "email": "volunteer2@example.com",
    #             "user_type": "volunteer",
    #             "first_name": "Jane",
    #             "last_name": "Smith",
    #             "gender": "Female",
    #             "phone_number": "9876543210",
    #             "interests": "Humanitarian causes",
    #         },
    #         {
    #             "email": "volunteer3@example.com",
    #             "user_type": "volunteer",
    #             "first_name": "Michael",
    #             "last_name": "Johnson",
    #             "gender": "Male",
    #             "phone_number": "5555555555",
    #             "interests": "Animal causes",
    #         },
    #     ]
    #

    def handle(self, *args, **options):
        sponsor_data = [
            {
                "user": AppUser.objects.get(email='sponsor1@ex.com'),
                "company_name": "ABC Corp",
                "website": "https://www.abccorp.com",
                "career_field": "Technology",
            },
            {
                "user": AppUser.objects.get(email='sponsor2@ex.com'),
                "company_name": "XYZ Ltd",
                "website": "https://www.xyzltd.com",
                "career_field": "Finance",
            },
            {
                "user": AppUser.objects.get(email='sponsor3@ex.com'),
                "company_name": "GreenCo",
                "website": "https://www.greenco.com",
                "career_field": "Environmental",
            },
        ]

        volunteer_data = [
            {
                "user": AppUser.objects.get(email='volunteer1@ex.com'),
                "first_name": "John",
                "last_name": "Doe",
                "gender": "Male",
                "bio": "Greetings, I'm Michael! Environmental stewardship is my calling, and I'm on a mission to protect and preserve our planet. As an eco-conscious volunteer, I'm always out there planting trees, cleaning up plastic waste, and raising awareness about sustainability. Armed with my background in environmental science, I'm dedicated to inspiring others to join me in building a greener, healthier world.",
                "phone_number": "0889787565",
                "interests": "Environmental causes",
            },
            {
                "user": AppUser.objects.get(email='volunteer2@ex.com'),
                "first_name": "Michael",
                "last_name": "Johnson",
                "profile_picture": "/static/images/volunteer2.jpg",
                "gender": "Female",
                "bio": "Hey there, I'm John! I'm all about being the change I wish to see in my community. With a background in education, I'm a firm believer in the transformative power of knowledge. I love organizing workshops and community events to empower others. Through mentoring programs and tutoring, I hope to inspire and uplift the next generation, creating a brighter future for us all.",
                "phone_number": "0898765432",
                "interests": "Humanitarian causes",
            },
            {
                "user": AppUser.objects.get(email='volunteer3@ex.com'),
                "first_name": "Jane",
                "last_name": "Smith",
                "profile_picture": "/static/images/Veronika.png",
                "gender": "Male",
                "bio": "Hi, I'm Jane! I'm a devoted volunteer with a deep passion for making a difference in the lives of those around me. As a social worker, I believe in the power of community service to bring positive change. From lending a helping hand at local food drives to mentoring young minds, my goal is to contribute to a better world through acts of kindness and compassion.",
                "phone_number": "0887878676",
                "interests": "Animal causes",
            },
        ]

        member_data = [
            {
                "user": AppUser.objects.get(email='member1@ex.com'),
                "first_name": "Emily",
                "last_name": "Williams",
                "profile_picture": "/static/images/member1.jpg",
                "gender": "Female",
                "phone_number": "+359886456767",
                "interests": "Environmental causes",
                "role": "Administrator",
            },
            {
                "user": AppUser.objects.get(email='member2@ex.com'),
                "first_name": "Daniel",
                "last_name": "Brown",
                "profile_picture": "/static/images/member2.jpg",
                "gender": "Male",
                "phone_number": "0899565745",
                "interests": "Humanitarian causes",
                "role": "Moderator",
            },
            {
                "user": AppUser.objects.get(email='member3@ex.com'),
                "first_name": "Olivia",
                "last_name": "Miller",
                "gender": "Female",
                "phone_number": "+359878565743",
                "interests": "Animal causes",
                "role": "PR",
            },
        ]
        sponsor_profile_instances = [SponsorProfile(**data) for data in sponsor_data]
        volunteer_profile_instances = [VolunteerProfile(**data) for data in volunteer_data]
        member_profile_instances = [MemberProfile(**data) for data in member_data]
        SponsorProfile.objects.bulk_create(sponsor_profile_instances)
        VolunteerProfile.objects.bulk_create(volunteer_profile_instances)
        MemberProfile.objects.bulk_create(member_profile_instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in user_profiles_... table.'))
