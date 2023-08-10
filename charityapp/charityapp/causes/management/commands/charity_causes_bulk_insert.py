from django.core.management.base import BaseCommand

from charityapp.causes.models import CharityCause


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        charity_data = [
            {
                'name': 'Recycling for Future',
                'resume': 'The number one goal of the campaign is to be good for our environment! Plastic bottles, aluminum and iron jugs and recyclable plastic are collected and with the funds collected separate collection facilities are purchased for the city.',
                'image': '/static/images/Recycling.jpg',
                'description': 'The campaign is conducted with the aim of caring for the environment and turning our trash into something valuable. We collect waste that can be recycled, then pass it on to secondary raw materials, and with the funds generated, we aim to purchase the first scavenger for the city of Kyustendil. The campaign collects flower pots, plastic bottles, powder cans, cheese buckets, cassettes, jugs, household buckets, fabric softener cans, plastic chairs, heavy duty nylon and cling film. Everything submitted to the campaign must be clean and crushed.',
                'motivation': 'Let`s nurture the nature so that we can have a better future',
                'type': 'Environmental Charity',
                'website': 'https://www.facebook.com/events/1168917804019909',
                'start_datetime': '2022-11-27 10:00',
                'end_datetime': '2022-11-27 13:00',
            },
            {
                'name': 'Blood donation for Future',
                'resume': 'The campaign aims to build the habit of free blood donation in the society. For people without contraindications, this is not only an act of kindness, but also beneficial for themselves.',
                'image': '/static/images/Blood Donation.jpg',
                'description': 'What do we need to know if we want to donate blood? Candidate blood donors must feel healthy, well rested, have eaten and taken fluids before donating blood (it is best to have fast carbohydrates and fluids - for example a sandwich and fruit juice/ compote) at least an hour before that; be aged between 18 and 60 years, weighing more than 50 kg (for women) and more than 60 kg (for men); have not taken any medication 48 hours prior to donation; have not donated blood less than 2 months ago; ladies should not be on their monthly cycle; have not undergone a surgical intervention in less than 1 year; do not have myopia with a diopter higher than 5; have not had a tattoo or piercing in less than 6 months; have not visited countries where malaria and other insect-borne and blood-borne infections are widespread; do not have an endocrine disease, allergic symptoms or a disease of the cardiovascular system, etc.; have no health problems (as judged on the spot by a medical team); have not recovered from COVID-19 in less than 40 days. After donating blood, it is recommended to take more caloric liquids and foods and, if necessary, rest. Participants in the campaign: will receive results of the tests of the blood donated by them (blood group, AIDS, hepatitis B and C and syphilis; they have the opportunity for up to 6 months for their blood donation to be recognized at the local level for the upcoming treatment of a close or relative in need; have the right to use 2 calendar days of additional leave.',
                'motivation': 'Be empathetic! Support life! Save lives!',
                'type': 'Humanitarian Charity',
                'website': 'https://www.facebook.com/events/703408561397601',
                'start_datetime': '2022-12-05 08:30',
                'end_datetime': '2022-12-05 15:30',
            },
            {
                'name': 'Recycling for Future vol.002',
                'resume': 'In this campaign we also collect batteries to support another noble initiative. Plastic bottles, aluminum and iron jugs and recyclable plastic are collected and with the funds collected separate collection facilities are purchased for the city.',
                'image': '/static/images/Recycling2.jpg',
                'description': 'The campaign is conducted with the aim of caring for the environment and turning our trash into something valuable. We collect waste that can be recycled, then pass it on to secondary raw materials, and with the funds generated, we aim to purchase the first scavenger for the city of Kyustendil. The campaign collects flower pots, plastic bottles, powder cans, cheese buckets, cassettes, jugs, household buckets, fabric softener cans, plastic chairs, heavy duty nylon, cling film and glass. Everything submitted to the campaign must be clean and crushed.',
                'motivation': 'Let`s nurture the nature so that we can have a better future',
                'type': 'Environmental Charity',
                'website': 'https://www.facebook.com/events/886111225907413',
                'start_datetime': '2023-02-05 10:00',
                'end_datetime': '2023-02-05 13:00',
            },
            {
                'name': 'Let`s bring back the heart of the square',
                'resume': 'The campaign aims to promote separate collection facilities in the city. During the campaign, in addition to a heart for caps, a container for plastic bottles and one for aluminum jugs will also be placed at the center.',
                'image': '/static/images/Heart.jpg',
                'description': 'After the necessary repair of the HEART for caps, located in "Velbuzhd" square, it`s time to return it back to its place! But that`s not all! His "faithful friends" will be placed next to him: a press for metal jugs of drinks - KENCHOYAD, and a "container" for separate collection of plastic bottles - SHISHEYAD! The caps and jugs collected will go to support the "Caps for the Future" campaign, and the bottles will support the "Club for the Future - Kyustendil".',
                'motivation': 'Let`s be responsible for nature and the environment we live in, and also support a good cause!',
                'type': 'Environmental Charity',
                'website': 'https://www.facebook.com/events/1278713872996277',
                'start_datetime': '2023-03-12 12:00',
                'end_datetime': '2023-03-12 13:00',
            },
            {
                'name': 'Caps for Future vol.005',
                'resume': 'The campaign is 2 in 1 - "Caps for the Future" and "Recycling for the Future - vol.003". We are collecting caps and aluminum jugs that will go to support the "Caps for the Future" campaign. We collect plastic bottles, recyclable plastics and glass, which will support our club - Club for the Future.',
                'image': '/static/images/Caps.jpg',
                'description': 'A quick reminder of what we collect in the "Caps for the Future" campaigns: CAPS any caps with the number 2 PE or 5 PP in a triangle on the inside; from drinks (water, milk, beer, soft drinks, juice, etc.);from hygiene preparations (shower gel, shampoo, detergents and fabric softeners, etc.);plastic bottles of medicine or chewing gum (from dense plastic number 2 PE or 5 PP);bottles of washing and cleaning agents (made of solid plastic number 2 PE or 5 PP). ALUMINUM SNAPSaluminum jugs of beer and soft drinks with the sign 41 ALU;Jugs marked 40 FE are NOT accepted;Cans of formula milk, cat/dog food are NOT accepted. We ask you to WASH AND CLEAN the raw materials collected by you, only in this way the recycling would be successful! We ask you to CRUSH the aluminum jugs as much as possible! It is RECOMMENDED that the caps are in tight bags. It is ABSOLUTELY FORBIDDEN to have sharp objects, medical supplies and any dangerous objects our health, and yours too! We look forward to seeing you at the campaign on April 22 to make the purchase of the FIFTH neonatal ambulance a success. We believe that TOGETHER WE CAN DO MORE!',
                'motivation': 'Providing the fifth, specialized by all standards, children\'s neonatal ambulance that will serve several areas.',
                'type': 'Environmental Charity',
                'website': 'https://www.facebook.com/events/1313830989475080',
                'start_datetime': '2023-04-22 10:00',
                'end_datetime': '2023-04-22 14:00',
            },

            {
                'name': 'Textile for Future vol.001',
                'resume': 'The campaign collects unnecessary textiles in order to prolong their life or recycle them! We see a number of advantages in the cause: You can get rid of unnecessary textiles, TexCycle will find the most suitable way to recover them, and we will be calm that the textiles will not end up in general waste, which pollutes nature!',
                'image': '/static/images/Textile.jpg',
                'description': 'We accept: clothes, shoes, bags, accessories (belts, scarves, hats, etc.), home textiles (sheets, towels, pillows, etc.) We do NOT accept: textile products contaminated with dangerous chemicals;carpets;quilts;mattresses;any large textile products. IMPORTANT: Textiles must be WASHED and NOT contaminated with dangerous chemicals! Knowing that the consumption of textiles is one of the main polluters of the environment, we believe in the meaning of a campaign like this and hope that more people will get involved! Can not wait to see you! Together we can and do create miracles!',
                'motivation': 'Providinf the fifth, specialized by all standards, children\'s neonatal ambulance that will serve several areas.',
                'type': 'Environmental Charity',
                'website': 'https://www.facebook.com/events/922045349015308',
                'start_datetime': '2023-05-20 12:00',
                'end_datetime': '2023-05-20 15:00',
            },

            {
                'name': 'Caps for Future vol.004',
                'resume': 'We are collecting caps and aluminum jugs that will go to support the "Caps for the Future" campaign. We collect plastic bottles, recyclable plastics and glass, which will support our club - Club for the Future.',
                'image': '/static/images/Caps.jpg',
                'description': 'A quick reminder of what we collect in the "Caps for the Future" campaigns: CAPS any caps with the number 2 PE or 5 PP in a triangle on the inside; from drinks (water, milk, beer, soft drinks, juice, etc.);from hygiene preparations (shower gel, shampoo, detergents and fabric softeners, etc.);plastic bottles of medicine or chewing gum (from dense plastic number 2 PE or 5 PP);bottles of washing and cleaning agents (made of solid plastic number 2 PE or 5 PP). ALUMINUM SNAPSaluminum jugs of beer and soft drinks with the sign 41 ALU;Jugs marked 40 FE are NOT accepted;Cans of formula milk, cat/dog food are NOT accepted. We ask you to WASH AND CLEAN the raw materials collected by you, only in this way the recycling would be successful! We ask you to CRUSH the aluminum jugs as much as possible! It is RECOMMENDED that the caps are in tight bags. It is ABSOLUTELY FORBIDDEN to have sharp objects, medical supplies and any dangerous objects our health, and yours too! We look forward to seeing you at the campaign on April 22 to make the purchase of the FIFTH neonatal ambulance a success. We believe that TOGETHER WE CAN DO MORE!',
                'motivation': 'Providing the fifth, specialized by all standards, children\'s neonatal ambulance that will serve several areas.',
                'type': 'Environmental Charity',
                'website': 'https://www.facebook.com/events/1313830989475080',
                'start_datetime': '2022-10-28 10:00',
                'end_datetime': '2022-10-28 14:00',
            },
        ]

        charity_instances = [CharityCause(**data) for data in charity_data]
        CharityCause.objects.bulk_create(charity_instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in work_charitycampaigns table.'))
