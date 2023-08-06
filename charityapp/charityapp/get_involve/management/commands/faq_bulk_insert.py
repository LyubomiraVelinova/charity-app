from django.core.management.base import BaseCommand

from charityapp.work.models import FAQ, CharityCampaign


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        faq_data = [
            {
                'campaigns': ['Recycling for Future', 'Recycling for Future vol.002'],
                'question': 'What is the main objective of the "Recycling for Future Campaigns"?',
                'answer': 'The main objective of the "Recycling for Future Campaigns" is to promote responsible waste management and environmental sustainability. We collect recycled garbage, such as glass jars, bottles, cans, and PET bottles, and turn them into valuable resources by selling them for scrap. The funds earned from recycling are then used to purchase bins for the city, creating a cleaner and greener environment.',
            },
            {
                'campaigns': ['Recycling for Future', 'Recycling for Future vol.002'],
                'question': 'What types of recyclable items are accepted in the campaign?',
                'answer': 'We accept a wide range of recyclable items, including glass jars (including children`s purees), bottles, cans (such as infant formula cans and dog/cat food cans), and PET bottles from soft drinks and beer (with "ALU" written on them). These items have a significant environmental impact, and by recycling them, we can contribute to a more sustainable future.',
            },
            {
                'campaigns': ['Recycling for Future', 'Recycling for Future vol.002'],
                'question': 'How can I participate in the campaign and contribute my recyclable items?',
                'answer': 'Participating in the "Recycling for Future Campaigns" is easy! Simply collect your recyclable items, such as glass jars, bottles, cans, and PET bottles, and bring them to our designated collection points. Stay tuned for announcements on our website and social media channels to find the nearest collection points and campaign dates.',
            },
            {
                'campaigns': ['Recycling for Future', 'Recycling for Future vol.002'],
                'question': 'What happens to the recyclable items after they are collected?',
                'answer': 'Once we collect the recyclable items, we carefully sort and prepare them for recycling. Glass, cans, and PET bottles are then sold to recycling facilities to be processed and turned into new materials. The funds generated from these recycling efforts are used to purchase bins for our city, contributing to a cleaner and more sustainable environment.',
            },
            {
                'campaigns': ['Recycling for Future', 'Recycling for Future vol.002'],
                'question': 'How does recycling contribute to environmental conservation and social impact?',
                'answer': 'Recycling plays a vital role in conserving natural resources and reducing waste in landfills. By participating in our recycling campaigns, you are actively contributing to waste reduction and minimizing the environmental burden. Moreover, the funds raised from recycling directly support our mission of providing bins for the city, enhancing waste management infrastructure, and promoting a cleaner and healthier living environment for all residents.',
            },
            {
                'campaigns': ['Recycling for Future', 'Recycling for Future vol.002'],
                'question': 'Can I volunteer to help with the "Recycling for Future Campaigns"?',
                'answer': 'Absolutely! We welcome volunteers who are passionate about environmental sustainability and want to make a difference in their community. If you are interested in volunteering for our recycling campaigns, please get in touch with our team through our website or contact information. Together, we can create a positive impact on the environment and our city.',
            },

            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'What is the purpose of the "Caps for Future" campaign?',
                'answer': 'The main goal of the "Caps for Future" campaign is to collect plastic caps and lids, recycle them into secondary raw materials, and use the funds generated to purchase incubators for premature babies or children\'s neonatal ambulances. By participating, you are not only contributing to environmental sustainability but also supporting the health and well-being of our little ones.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'What types of plastic caps and lids can I contribute?',
                'answer': 'We accept various types of plastic caps, rings, and handles from beverage bottles, including plastic bottles of mineral water, beer, soft drinks, milk, and juice. Additionally, we collect caps and dispensers of plastic cartons of milk and juice.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'Can I contribute lids of jars suitable for food and drink storage?',
                'answer': 'Yes, we do collect lids (which bend) of jars suitable for food and drink storage. However, please note that they are collected separately from the caps and only in Sofia and Kyustendil.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'Are there any specific guidelines for contributing lids and/or boxes of ice cream and other food products?',
                'answer': 'Yes, we accept lids and/or boxes of ice cream and other food products, but only if they are made of plastic labeled with the numbers 2 or 5. Please remember that these items are collected separately from the caps and only in Sofia and Kyustendil.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'Can I contribute spoons from infant formula products?',
                'answer': 'Certainly! We welcome the contribution of spoons (which bend) from infant formula products.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'What should I avoid contributing during the campaign?',
                'answer': 'To maintain the efficiency of our recycling process, please refrain from bringing metal caps, batteries, any small and large plastic objects, dirty dishes from food, needles, syringes, food waste, and other non-recyclable items.',
                'important': '*This way you protect not only the machines of the recyclers, but also the health of the volunteers. This allows us to do the important stuff (like collecting and loading the caps) during the campaigns!',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'How should I collect and transport the caps?',
                'answer': 'You can collect the caps in any container you find convenient. However, during our campaigns, we greatly appreciate it if you use thick garbage bags or burlap sacks. Our volunteers reuse these bags when emptying the hearts of the campaign. Avoid using cartons and paper bags, as they can tear easily, leading to caps being scattered during transport.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'Can I use large bottles to collect the caps?',
                'answer': 'While large bottles might seem like a convenient option, we kindly ask you not to collect caps in them. Large bottles create challenges during the recycling process, and additional efforts are required to process them. Opt for using the recommended containers to make our recycling process more efficient.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'How can I find the nearest collection points for the caps?',
                'answer': 'We regularly update our website and social media platforms with information about collection points in different locations. Please check our website or social media channels to find the nearest collection points to you.',
            },
            {
                'campaigns': ['Caps for Future vol.004', 'Caps for Future vol.005'],
                'question': 'How often do you run the "Caps for Future" campaign?',
                'answer': 'The "Caps for Future" campaign runs regularly twice a year, and we encourage everyone to participate in every campaign to make a meaningful impact on our environment and the lives of our little ones.',
            },

            {
                'campaigns': ['Textile for Future vol.001', ],
                'question': "What is the 'Textile for Future' campaign all about?",
                'answer': "The 'Textile for Future' campaign is a collaborative initiative in partnership with 'TextCycle' aimed at promoting responsible textile recycling. We collect various types of textiles, including clothing, shoes, bags, accessories (belts, scarves, hats, etc.), and home textiles (sheets, towels, pillows, etc.). Through this campaign, we aim to divert textiles from landfills and work with 'TextCycle' to find the best way to recycle and repurpose each textile attribute.",
            },
            {
                'campaigns': ['Textile for Future vol.001', ],
                'question': 'How does the textile recycling process work?',
                'answer': 'Once we collect the textiles, we work closely with our partner "TextCycle" to ensure each textile\'s proper recycling. "TextCycle" employs specialized techniques to determine the best way to handle each textile attribute. They separate wearable items from those suitable for upcycling or repurposing. By engaging in this eco-friendly process, we help reduce textile waste and its impact on the environment.',
            },
            {
                'campaigns': ['Textile for Future vol.001', ],
                'question': 'What types of textiles are accepted in the campaign?',
                'answer': 'We accept a wide range of textiles, including clothing, shoes, bags, accessories (belts, scarves, hats, etc.), and home textiles (sheets, towels, pillows, etc.). These items hold potential for recycling or repurposing, contributing to a more sustainable fashion industry and reducing textile waste.',
            },
            {
                'campaigns': ['Textile for Future vol.001', ],
                'question': 'What should participants avoid donating in the "Textile for Future" campaign?',
                'answer': 'To ensure the success of our recycling efforts, we kindly request participants not to donate textiles contaminated with hazardous chemicals, such as oil or paint stains. Additionally, we do not collect carpets, quilts, mattresses, or any large textile products. Focusing on suitable textiles ensures a more efficient and sustainable recycling process.',
            },
            {
                'campaigns': ['Textile for Future vol.001', ],
                'question': 'How can I participate in the "Textile for Future" campaign?',
                'answer': 'Participating in the "Textile for Future" campaign is easy! Gather your unwanted textiles, including clothing, shoes, bags, and home textiles, and bring them to our designated collection points. Follow our website and social media channels for updates on the campaign dates and locations.',
            },
            {
                'campaigns': ['Textile for Future vol.001', ],
                'question': 'What impact does textile recycling have on the environment and communities?',
                'answer': 'Textile recycling significantly reduces the environmental impact of the fashion industry by diverting textiles from landfills and incineration. By recycling textiles, we conserve valuable resources, save energy, and reduce greenhouse gas emissions. Moreover, our partnership with "TextCycle" ensures that wearable textiles find new life, benefiting local communities and organizations in need.',
            },
            {
                'campaigns': ['Textile for Future vol.001', ],
                'question': 'Can I support the "Textile for Future" campaign as a volunteer?',
                'answer': 'Absolutely! We welcome volunteers who share our passion for sustainable fashion and responsible textile management. If you wish to contribute your time and effort to the "Textile for Future" campaign, reach out to us through our website or contact information. Together, we can create a positive impact on the environment and pave the way for a more sustainable future.',
            },

            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'Who can donate blood?',
                'answer': "Any healthy person aged 18 to 65 years who weighs more than 50 kg, has not taken any medication for at least 48 hours and for whom a doctor has judged that donating blood does not endanger his health and the blood he donates is safe for sick, needy from her, can become a donor. Men can donate blood 5 times within a calendar year, and women - 4 times, and the interval between two blood donations must be at least 2 months.",
            },
            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'How to prepare for donating blood?',
                'answer': "Two or three days before the act of donating blood, a person should eat regularly and in a varied way - this strengthens the body's strength and increases the quality of the blood. Donating blood should not be done on an empty stomach. The blood donor must be sure that he is healthy and rested. After donating blood, more caloric liquids and foods are taken.",
            },
            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'What is the procedure for donating blood?',
                'answer': "A questionnaire is filled out about your health status. They follow: • Examination and personal conversation with a doctor. • Preliminary examination of the candidate blood donor - a few drops of blood are taken from the finger for express determination of blood group and hemoglobin. If the hemoglobin is below 125 g/l for women and below 135 g/l for men, blood donation is not allowed. • Blood donation - the amount of donated blood is between 405 and 450 ml. The bag in which it is collected has a special solution with a volume of 63 ml. It maintains the life of blood cells and thanks to it, blood and blood components retain their healing properties for up to 36 days. Important: If the donor feels unwell during the blood donation, the blood collection process is suspended. In this case, the donated blood does not have the qualities to be transfused to a patient, but it is not discarded. It is used for the production of blood products with a certain healing effect. The described procedure lasts a maximum of 40 minutes.",
            },
            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'What is recommended after donating blood?',
                'answer': "The compression bandage should remain on your arm for at least 2 (two) hours. We recommend that you do not smoke for at least 2 (two) hours after the blood collection is completed. Do not put any strain on the lancing arm for at least 4 (four) hours after the blood collection is completed. Try to take more caloric liquids and foods in the first 3 (three) days after the blood collection. During the first 24 hours, the volume of blood taken is completely restored. Vegetarian food does not interfere with recovery. In the first hours after donating blood, avoid highly smoky, high-temperature and humid rooms. Those of you who carry out professional or recreational risky activities (piloting airplanes, driving buses or trains, operating cranes, climbing escalators or scaffolding, hang gliding, climbing and diving) should wait at least 12 hours before to return to them. In case of accidental health complaints that you associate with the blood donation process, please call +359 2 9210 477 during the working hours of the NCTH or contact your personal physician.",
            },
            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'How long does it take for the blood to recover?',
                'answer': "Quantitatively, the blood is restored in about a day, and qualitatively - in 3-4 weeks.",
            },
            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'Important for blood donation',
                'answer': "According to the regulations in the Republic of Bulgaria, donated blood is used for the treatment of patients only within the borders of the country (in rare exceptions and for seriously injured compatriots abroad). The blood donor donates 450 ml. blood. All consumables used during blood donation are individual, sterile and disposable. There is no possibility of contracting AIDS or any other blood-borne infection. Donating blood is helpful. It stimulates the renewal process of blood cells and increases the body's defenses. Blood donors receive 2 days of paid leave (Article 157, Para. 1, Item 2 of the Labor Code), a complementary breakfast and a gift, and if they wish to do so, the results of tests for AIDS, hepatitis B and C, syphilis and blood group.",
            },
            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'Who needs donated blood?',
                'answer': "Blood is used for the treatment of patients with acute blood loss caused by trauma, for the treatment of severe burns, for planned and emergency surgical and obstetric interventions, for AB0 and Rh incompatibility of the mother and fetus, for the treatment of malignant diseases, as well as for maintaining the lives of patients with various congenital anemias and hemophilias.",
            },
            {
                'campaigns': ['Blood donation for Future', ],
                'question': 'Who cannot donate blood?',
                'answer': "People who suffer from diseases such as AIDS, hepatitis, syphilis, tuberculosis, toxoplasmosis, brucellosis, otosclerosis and Meniere's syndrome, bronchitis, allergies, chronic osteomyelitis and bone deformities, rheumatism, stomach or duodenal ulcer, psoriasis, eczema on skin, glaucoma, etc. All acute infectious diseases are contraindicated (during illness and the convalescent period). People who have had contact with infectious patients - for a period equal to the incubation period - cannot donate blood either. A problem is the presence of cardiovascular disease, tropical infections, bone marrow, kidney and liver problems. Blood donation is also not carried out in cases where, at the discretion of the doctor or the certifying person, this act of sympathy poses a danger to the health of the donor.",
            },
        ]
        for data in faq_data:
            # Create the FAQ instance
            faq_instance = FAQ.objects.create(
                question=data['question'],
                answer=data['answer']
            )

            # Add the related campaigns to the FAQ instance
            for campaign_name in data.get('campaigns', []):
                try:
                    campaign = CharityCampaign.objects.get(name=campaign_name)
                    faq_instance.campaigns.add(campaign)
                except CharityCampaign.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Campaign "{campaign_name}" does not exist.'))

        self.stdout.write(self.style.SUCCESS('Data inserted successfully in table work_faq.'))
