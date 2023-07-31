from django.core.management import BaseCommand

from charityapp.common.models import LatestNews


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        latest_news_data = [
            {
                'event_date': '2023-07-30',
                'title': 'The Fifth Children`s Neonatal Ambulance',
                'description': 'The fifth children`s neonatal ambulance is 95% ready. It will be donated soon!'
            },
            {
                'event_date': '2023-07-29',
                'title': 'The second mountain off-road #ambulance',
                'description': 'The second mountain off-road ambulance of "Caps for the Future" is 99% ready! Expect very soon!'
            },
            {
                'event_date': '2023-07-29',
                'title': 'Recent days many transported babies',
                'description': 'In recent days, the CapsForFuture ambulance in Plovdiv has been transporting babies in need to Plovdiv or Sofia literally every day! Thank you!'
            },
            {
                'event_date': '2023-07-28',
                'title': 'Transported baby from Parvomai',
                'description': 'A baby was born on 28.07.2023 in Parvomai, but it turned out to have respiratory problems. He had to be urgently transported to Plovdiv! From there, they immediately sent the #CapsForFuture ambulance! It was necessary to act very quickly!'
            },
            {
                'event_date': '2023-06-10',
                'title': 'Donated transport incubator in Kyustendil',
                'description': 'With an oxygen module, with an air humidifier, with a heating system, sensors for the temperature of the air and the baby`s skin, a battery for when there is no electricity nearby, a comfortable stroller ... Donated to the hospital in Kyustendil by all the people who they help CapsForTheFuture.'
            },
            {
                'event_date': '2023-05-07',
                'title': 'Baby from Velingrad',
                'description': 'On 03.07.2023, a SEVENTH MONTH woman in labor arrived at the hospital in Velingrad with a detached placenta!! After an emergency C-section, a little one appears in the world, however, in a critical condition. The doctors had to drain nearly 200ml of blood from the baby`s stomach, after which the little hero was intubated and with the help of the incubator donated by #CapsForFuture and the local Lion`s Club, he was successfully transported to the hospital in Pazardzhik! Mother and baby are fine!'
            },
            {
                'event_date': '2023-05-26',
                'title': 'Baby from Karlovo',
                'description': 'A baby was born on 26.05.2023 in Karlovo with respiratory failure. The CapsForFuture ambulance from Plovdiv is leaving immediately! In it are Dr. Koichev, senior nurse Ikimova and paramedic Ivan Lesov, who is one of the people who most often travel with the ambulance. The medics took the baby, breathed him all the way and successfully transported him to the neonatology unit at St. George in Plovdiv. Another successful mission for the ambulance and its team. Another life saved!'
            },
            {
                'event_date': '2023-05-19',
                'title': ' Donated monitors in Burgas',
                'description': 'On 19.05.2023 we helped to the invasive cardiology department in Burgas to monitor the condition of those treated there by new and advanced vital signs monitors.'
            }, {
                'event_date': '2023-05-15',
                'title': 'Transported twins from Velingrad',
                'description': 'On 15.05.2023 the transport incubator that #CapsForFuture donated to the hospital in Velingrad, together with the local Lion`s Club, carried out another successful mission by transporting two newborn twins - each weighing less than 2 kg - to the hospital in Pazardzhik ❤ So far, the incubator has helped close to 60 children to safely pass the bends between Velingrad and Pazardzhik.'
            },
        ]

        instances = [LatestNews(**data) for data in latest_news_data]
        LatestNews.objects.bulk_create(instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in table common_latestnews.'))
