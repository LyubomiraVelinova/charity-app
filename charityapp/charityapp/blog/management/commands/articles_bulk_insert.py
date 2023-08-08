from django.core.management.base import BaseCommand

from charityapp.accounts.models import AppUser
from charityapp.blog.models import Article


class Command(BaseCommand):
    help = 'Bulk insert data into the database.'

    def handle(self, *args, **options):
        article_data = [
            {
                'title': 'Sustainable Travel',
                'subtitle': 'Exploring Responsibly',
                'introduction': 'As nature lovers and responsible travelers, we hold a special responsibility to protect the environment and minimize our impact on the places we visit. In this article, we embark on a journey of sustainable travel practices that will help us explore the world while leaving behind a positive footprint.',
                'short_resume': 'Learn sustainable travel tips, from eco-friendly accommodations to wildlife conservation, to minimize your environmental impact while exploring the world.',
                'content': 'Choosing Eco-Friendly Accommodations:Learn how to select eco-friendly hotels, lodges, or eco-resorts that prioritize sustainability, energy efficiency, and conservation efforts. We`ll explore various eco-certifications and green initiatives that accommodation providers may adopt to promote responsible travel. Mindful Transportation Options:Discover eco-conscious transportation options, such as public transit, biking, or walking, to reduce carbon emissions during our travels. We`ll explore the benefits of using alternative transportation and how it adds to the adventure of exploring new destinations.Respectful Wildlife Encounters:Understand the importance of responsible wildlife tourism and ethical animal encounters. We`ll discuss ways to support sanctuaries and reserves that prioritize the well-being of animals and their natural habitats, rather than exploitative practices.Embracing Sustainable Travel Gear:Explore eco-friendly travel gear, from reusable water bottles and biodegradable toiletries to sustainable luggage options. We`ll highlight how these small choices can collectively contribute to reducing plastic waste and promoting a greener future.',
                'author': AppUser.objects.get(email='Tatyana@abv.bg'),
                'featured_image': 'https://mdbootstrap.com/img/new/standard/nature/022.jpg',
            },

            {
                'title': 'Harmful Usage of Plastic Bags',
                'subtitle': 'A Call for Conscious Consumption',
                'introduction': 'In this eye-opening article, we shed light on the detrimental effects of plastic bags on the environment and wildlife. We`ll delve into the alarming statistics and discuss why it`s crucial to address our dependence on single-use plastics.',
                'short_resume': 'Discover the devastating effects of plastic bags on the environment and wildlife, and find alternatives to reduce single-use plastic consumption.',
                'content': 'The Environmental Impact:Understand the lifecycle of plastic bags and their devastating impact on marine life, land ecosystems, and our oceans. We`ll also explore the role of microplastics in the food chain and its potential harm to human health.Solutions and Alternatives:Discover practical alternatives to single-use plastic bags, including reusable bags made from sustainable materials like cotton, jute, or recycled plastics. We`ll provide tips on incorporating eco-friendly shopping habits into our daily lives.',
                'author': AppUser.objects.get(email='Lyubomirttta@abv.bg'),
                'featured_image': 'https://images.unsplash.com/photo-1621448835648-fe3488ada89b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=735&q=80',
            },

            {
                'title': 'The Power of Recycling',
                'subtitle': 'Paving the Path to a Greener Future',
                'introduction': 'Recycling plays a crucial role in waste management and environmental conservation. In this informative article, we`ll dive into the significance of recycling and how it contributes to resource conservation.',
                'short_resume': 'Explore the importance of recycling in conserving resources and reducing waste, and learn how to be a responsible recycler in your community.',
                'content': 'Understanding the Recycling Process:Explore the step-by-step process of recycling and how various materials like paper, plastic, glass, and metal are repurposed into new products. We`ll emphasize the importance of separating recyclables and reducing contamination.Benefits of Recycling:Learn about the environmental benefits of recycling, including energy conservation, greenhouse gas reduction, and the preservation of natural resources. We`ll also highlight the economic advantages of recycling for communities and industries.',
                'author': AppUser.objects.get(email='l55@abv.bg'),
                'featured_image': 'https://plus.unsplash.com/premium_photo-1679728130451-ebba4dc5307d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=880&q=80',
            },

            {
                'title': 'The Plastic Predicament',
                'subtitle': 'Confronting Our Dependency',
                'introduction': 'Plastic has become an omnipresent aspect of modern life, but it comes with significant environmental challenges. In this thought-provoking article, we address the alarming issue of plastic pollution and the need for collective action.',
                'short_resume': 'Confront the global issue of plastic pollution, its impact on the environment, and how individuals can take action to reduce plastic usage.',
                'content': 'Plastic`s Environmental Toll:Understand the grave consequences of plastic pollution on marine life, terrestrial ecosystems, and human health. We`ll explore the scale of the problem and how plastic waste negatively impacts the entire planet.Individual Responsibility and Collective Action:Discuss the importance of reducing plastic consumption, advocating for plastic-free policies, and supporting initiatives that combat plastic pollution. We`ll encourage readers to take meaningful steps in their daily lives to minimize plastic usage.',
                'author': AppUser.objects.get(email='ljjhg@abv.bg'),
                'featured_image': 'https://images.unsplash.com/photo-1586041828039-b8d193d6d1dc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80',
            },

            {
                'title': 'Nature',
                'subtitle': 'Our Sacred Responsibility to Preserve',
                'introduction': 'Nature is a precious gift that requires our utmost care and protection. In this heartfelt article, we reflect on the intrinsic connection between humans and nature, emphasizing the urgency of preserving the Earth`s beauty and biodiversity.',
                'short_resume': 'Reflect on the intrinsic connection between humans and nature, and understand the urgency of preserving the Earth`s beauty and biodiversity.',
                'content': 'The Interconnected Web of Life:Explore the delicate balance of ecosystems and the vital role each living organism plays in sustaining the planet`s biodiversity. We`ll celebrate the wonders of nature and its profound impact on our well-being. Conservation Initiatives:Discover global and local conservation efforts that aim to protect natural habitats, endangered species, and biodiversity hotspots. We`ll inspire readers to get involved in conservation projects and initiatives in their communities.',
                'author': AppUser.objects.get(email='fre64e_kef4e_93@abv.bg'),
                'featured_image': 'https://images.unsplash.com/photo-1596203721435-47040fbf51a1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1135&q=80',
            },
        ]

        instances = [Article(**data) for data in article_data]
        Article.objects.bulk_create(instances)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully in table blog_article.'))
