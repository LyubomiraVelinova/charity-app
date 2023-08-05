from django.core.management.base import BaseCommand

from charityapp.work.models import DonationCampaign


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        donation_data = [
            {
                'title': 'Neonatal Ambulance Fund',
                'description': 'This campaign seeks to address the critical need for specialized transportation for newborns who require immediate medical attention. By donating to the Neonatal Ambulance Fund, supporters can contribute to saving the lives of vulnerable infants and ensure they receive timely medical care.',
                'goal_amount': 90000.00,
                'purpose': 'The purpose of this campaign is to raise funds specifically for purchasing neonatal ambulances or medical equipment dedicated to hospitals specializing in neonatal care. The campaign aims to improve neonatal healthcare services and provide timely transportation for premature and critically ill newborns to medical facilities.',
                'start_date': '2023-05-23',
                'end_date': '2023-07-17',
                'current_amount': 1800.00,
            },
            {
                'title': 'Mountain Ambulance Rescue Initiative',
                'description': 'This campaign focuses on recognizing the importance of mountain ambulance services in remote areas where access to medical facilities is challenging. By contributing to the Mountain Ambulance Rescue Initiative, donors can ensure that injured adventurers and locals receive timely medical attention and emergency transportation in mountainous regions.',
                'goal_amount': 55000.00,
                'purpose': 'The purpose of this campaign is to provide support to mountain ambulance services, which play a crucial role in rescuing and transporting injured hikers and climbers in remote mountainous areas. The campaign aims to enhance emergency response capabilities in challenging terrains.',
                'start_date': '2023-05-23',
                'end_date': '2023-07-17',
                'current_amount': 1800.50,
            },
            {
                'title': 'Recycle for a Greener Future',
                'description': '"Recycle for a Greener Future" campaign aims to encourage individuals and communities to adopt recycling as a responsible waste management practice. By donating to the campaign, supporters can contribute to creating a cleaner and greener environment, reducing the impact of waste on ecosystems and wildlife.',
                'goal_amount': 5500.00,
                'purpose': 'The purpose of this campaign is to promote recycling and environmental sustainability by providing recycling bins to communities and public spaces. The campaign aims to raise awareness about the importance of recycling in reducing waste and preserving the environment.',
                'start_date': '2023-05-23',
                'end_date': '2023-07-17',
                'current_amount': 1800.50,
            },
            {
                'title': 'First Aid Training for Children',
                'description': 'This campaign focuses on equipping children with essential first aid skills, such as basic CPR, injury treatment, and emergency response. By supporting the "First Aid Training for Children" campaign, donors can contribute to building a safer community and empowering children to be proactive in responding to emergencies.',
                'goal_amount': 16600.00,
                'purpose': 'The purpose of this campaign is to provide first aid training to children, empowering them with life-saving skills and knowledge. The campaign aims to promote safety and preparedness among the younger generation.',
                'start_date': '2023-05-23',
                'end_date': '2023-07-17',
                'current_amount': 1800.50,
            },
        ]

        donation_instances = [DonationCampaign(**data) for data in donation_data]
        DonationCampaign.objects.bulk_create(donation_instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in work_donationcampaigns table.'))
