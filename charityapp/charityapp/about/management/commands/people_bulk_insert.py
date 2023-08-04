from django.core.management.base import BaseCommand

from charityapp.about.models import People


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        people_data = [
            People(
                first_name='Vesela',
                last_name='Grozdanova',
                member_role='Coordinator of "Caps for the Future"',
                profile_picture='https://images.unsplash.com/photo-1594744803329-e58b31de8bf5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
                description='Vesela is our Assistant Coordinator for the Caps for the Future campaign - the person who is inextricably next to Silvia and helps with everything about the campaign since the second year the campaign has been held in the city. She knows how to make everything work, extremely responsive and dedicated to helping. Her priority is causes related to the purity of nature. Her big heart does not allow her to get angry/offensive and helps her to forgive easily. She is one of those people who will always respond if needed. It always helps!'
            ),

            People(
                first_name='Violina',
                last_name='Stoimenova',
                member_role='Cashier',
                profile_picture='https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
                description='Violina is our Cashier - the person to whom we have entrusted the responsibility for the money, she monitors the incoming and outgoing amounts. Violina is also our coordinator for the village of Zhilentsi. She is another person with a big heart with us. Her strengths are creativity, communication and persistence. Extremely responsible, organized and consistent. She knows how to organize groups of people, and she is very easy and pleasant to work with. She is dedicated and as a bonus to all this we will also add her sense of humor. Since Violina works in a community center, it has a room for storing caps and a stage for concerts and events. Has experience in previous work campaigns. She is interested in the world around her, knows how to see the problem and fights until she solves it.'
            ),

            People(
                first_name='Eleonara',
                last_name='Vasileva',
                member_role='PR',
                profile_picture='https://images.unsplash.com/photo-1488716820095-cbe80883c496?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=686&q=80',
                description='Eleonora is our PR - the person who presents our club the best. We owe the activity on the club page to her, she is the person behind this page and takes care of spreading our work. She is also the face of the club in front of the media. Apart from all the campaigns in the club, Eleonora gives her whole heart and soul to the causes she personally takes up. Eleonora is one of those people who will always find time, energy and motivation to help a person in need. So far, she has helped dozens of people in need and continues to do so. She not only completes every cause he takes up, but also boasts great results. Stubborn, purposeful, guided by a good heart, she has proven hundreds of times that there is reason to trust her unreservedly. He has enviable communication skills, knows how to infect people with his kindness and captivate people with his causes. He is also a partner of the "Clean Struma" cause and stands out as an indisputable activist for the city.'
            ),

            People(
                first_name='Iskra',
                last_name='Stoilova',
                member_role='Responsible for recycling',
                profile_picture='https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=761&q=80',
                description='Iskra is our recycling and waste recovery officer. The woman who for years thinks about nature and acts in harmony with it. Unanimously, we can all say that Iskra is fully committed to cleaning, recycling and recovering waste so that the world can one day be a cleaner place. A few years ago, Iskra started from scratch to collect plastic and "sell" it to second-handers, with which he managed to establish himself as the most active person related to the collection and utilization of waste for the city and its surroundings. Her strengths are ecology, knowledge of waste sorting, her sincerity, her creativity, her creativity and the ability to have a solution, a plan, a goal, an idea for every situation. Iskra often sets a clear path to follow with well-grounded goals. She is the person who makes contacts with secondary raw materials, the municipality and a bunch of organizations when it comes to cleaning or collecting waste for recycling. Iskra thinks and acts for nature, is a partner of the "Clean Struma" cause.'
            ),

            People(
                first_name='Lyubomira',
                last_name='Velinova',
                member_role='Secretary',
                profile_picture='https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
                description='Lubomira is our Secretary - the person who creates and manages the documentation related to the club and its activities. She is responsible, executive and consistent until she completes what she sets out to do. Can work with technology at an intermediate level, organize and arrange, work in a team. He likes to challenge himself and go outside his comfort zone. Has previous experience volunteering for various causes. She will go to work and participate in any cause, but those supporting people are her highest priority. Here\'s what else she says: "I want good to win, I hope and believe it will, but for that we need each of us to do a little good every day. Each of us is responsible for making the world a better place. a good place to live - from the smile you can give a stranger to the flower you can buy from the grandmother on the street.'
            ),

            People(
                first_name='Lyubomira',
                last_name='Sharbanova',
                member_role='Blood donation coordinator',
                profile_picture='https://images.unsplash.com/photo-1534751516642-a1af1ef26a56?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=689&q=80',
                description='Lubomira is our blood donation coordinator - the person we can count on for one of our most humanitarian causes. She is an extremely well-intentioned and balanced person. He has time, energy, strength and a great desire to participate in the creation of a better living environment. From her work, Lubomira has learned that before proposing a solution to something, the most important thing is to familiarize yourself with the process and not rely on assumptions. The main focus for Lubomira is the separate collection of waste, reducing our waste and the multiple use of facilities. She is responsible, extremely diligent and executive, persistent and empathetic. Able to empathize and empathize without blaming or pointing out faults. He understands well that everyone has the right to a position and accepts final opinions unconditionally. He is good at playing the role of a balancer in relationships. Lubomira is a man of action. He has experience in previous work initiatives as a volunteer. Here\'s what else he says about himself: “The things that bring me satisfaction are mainly related to being able to help someone / feeling useful. I am willing to help with any initiatives related to the improvement of our living environment, because change starts from within us. I strongly believe that the things we do for each other gratuitously, the examples we set, are the highest expression of the human in us and keep us moving in the right direction. And a story that is my favorite and stuck in my mind from the TED talks videos: "A soldier was asked what made him go to the front, help and cover another person he had just met, risking the most precious thing - his life? And he answered: "Because he would do it for me too!"'
            ),

            People(
                first_name='Silviq',
                last_name='Evtimova',
                member_role='Representative of "Caps for Future"',
                profile_picture='https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1287&q=80',
                description='Silvia is our Coordinator for the "Caps for the Future" campaign, she is also officially registered as a point. She is the first person to do the campaign in the town of Kyustendil, and the first year she does it all by herself, the second year Vesela helps her, and in the third Iskra, Eleonara, Zdravko and others are already involved. Fiercely motivated, totally dedicated to the Caps for the Future campaign, she even defines the campaign as the meaning of her life. She is one of those people who will give you a hand without knowing you and who only need a smile to have a wonderful day. She has very good organizational skills, she is responsible, and qualities such as humanity, kindness and wisdom are inherent to her. Sylvia takes the cause she has taken up to heart and tries to constantly ignite the spark in other people as well. Silvia would jump into any job that came her way - from collecting rubbish, sorting it, to helping people - she can do anything and she does it with all her dedication. Here\'s what else she says about herself: "I need very little to be happy. One smile. One kind word. And a lot of good people around me."'
            ),

            People(
                first_name='Zdravko',
                last_name='Velinov',
                member_role='Chairman',
                profile_picture='https://images.unsplash.com/photo-1568602471122-7832951cc4c5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80',
                description='Zdravko is our Chairman - the person with outstanding leadership qualities who unites us all. He is wholeheartedly committed to everything he undertakes (and believe me, he has undertaken many things) and does not settle for mediocre results. Hearty and open, extremely active and constantly fighting for Good, Zdravko is also involved in many other volunteer initiatives. He knows how to organize and arrange, he has well-developed spatial thinking. He would never judge a person, he accepts everyone as they are. For most campaigns, Zdravko designs the posters and takes care of their printing. He is also the creator of the club\'s logo. Here\'s what else he himself says about himself: "I\'m crazy, but if I believe in something, I hold on to it and strive to develop and improve it, this applies to me and I always strive to be better than yesterday, not only as a person, but as a thought and action. I don\'t give up easily, I believe in people and good, and I know that sooner or later it will win!"'
            ),

            People(
                first_name='Ivailo',
                last_name='Velinov',
                member_role='Vice-Chairman',
                profile_picture='https://images.unsplash.com/photo-1611608822650-925c227ef4d2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NzF8fG1hbnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=400&q=60',
                description='Ivaylo Velinov is our Deputy Chairman - the person who can overlap the responsibilities of the Chairman. He is also capable of uniting all club members when conflict arises. Open and honest, he takes any criticism to heart, keeps his word and (as they say) punches hard. He is serious and responsible for serious matters. He is ready to participate in any initiatives, has enviable communication skills, is purposeful and gives himself up for the good of people. He participated and participates as a volunteer in other initiatives. Ivaylo has been a volunteer mountain rescuer for many years, is resistant to bad weather conditions, knows how to react quickly and extremely adequately in critical situations. He has basic knowledge of medicine and first aid, and can work with ropes and climbing equipment. He does not accept failure, he is ready to fight long and hard to achieve his goals. Here\'s what else he says: "I strongly believe that humanity is in everyone, it just needs to be provoked adequately!"'
            ),

            People(
                first_name='Svetlin',
                last_name='Kirilov',
                member_role='Education Specialist',
                profile_picture='https://images.unsplash.com/photo-1557862921-37829c790f19?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1171&q=80',
                description='Svetlin is one of those people who perfectly understand that the future is in the hands of children, and we are responsible for their upbringing, their views and worldview. Therefore, he puts all his energy into being with the children, guiding them and showing them the right path. With a positive example and a creative approach, he manages to motivate and inspire his students, unfold their potential and participate in building a value system worthy of admiration. It is as if the words of Prof. Lalchev were spoken about him: "Because the teacher is the eternal engine of education. Through education, man reaches the greatest value of his life - knowledge. And knowledge is the light of the soul. But the sun of knowledge cannot rise without the driving force of the teacher." His interests focus on the socio-emotional education of young people; dedication, development and preservation of values and spirituality, not of materialism; virtue; nature and its purity, as well as many others. Svetlin is the person with proactive ideas in the club. He has many years of organizational experience in various campaigns, initiatives, projects and events, as well as serious experience in working and collaborating with students, institutions, NGOs, media and Dr. and field work. Extremely active, he is ready to help anyone who would ask for help. Here\'s what else he says about himself: "I do things to make others happy, then I start to feel that way too!"'
            ),
        ]

        People.objects.bulk_create(people_data)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in table about_people.'))
