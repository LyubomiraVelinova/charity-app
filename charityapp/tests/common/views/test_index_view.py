from django.test import TestCase
from django.urls import reverse

from charityapp.common.models import LatestNews
from charityapp.user_profiles.models import Testimonial


class IndexViewTests(TestCase):
    LATEST_NEWS_VALID_DATA = {
        'event_date': '2023-08-10',
        'title': 'Exciting Event Announcement',
        'description': 'We are pleased to announce an exciting event happening soon!',
    }

    def test_index__when_no_data__expect_empty_data(self):
        response = self.client.get(
            reverse('home-page'),
        )

        context = response.context

        self.assertEquals(200, response.status_code)
        self.assertEquals(0, len(context['charity_campaigns']))
        self.assertEquals(0, len(context['donation_campaigns']))
        self.assertEquals(0, len(context['act_green_blog']))
        self.assertTemplateUsed(response, 'common/home-page.html')

    def test_index__when_single_news__expect_empty_data(self):
        latest_news = LatestNews.objects.create(**self.LATEST_NEWS_VALID_DATA)
        latest_news.save()

        response = self.client.get(
            reverse('home-page'),
        )

        context = response.context

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, len(context['first_news']))
        self.assertTemplateUsed(response, 'common/home-page.html')
