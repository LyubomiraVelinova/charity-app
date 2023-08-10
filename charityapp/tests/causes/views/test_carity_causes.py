from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from charityapp.causes.models import CharityCause, FAQ
from charityapp.causes.views import CharityCausesView


class CharityCausesViewTest(TestCase):
    VALID_CHARITY_CAUSE_DATA_1 = {
        'name': 'Caps for Future',
        'resume': 'This is a summary of the campaign.',
        'description': 'This is the detailed description of the campaign.',
        'motivation': 'The motivation behind this campaign.',
        'type': 'Type of Charity',  # Replace with actual type
        'website': 'https://example.com',
        'start_datetime': timezone.now(),
        'end_datetime': timezone.now() + timedelta(days=30),
        'place': 'Example Location',
        'active': True,
    }
    VALID_CHARITY_CAUSE_DATA_2 = {
        'name': 'Recycling for Future',
        'resume': 'This is a summary of the campaign.',
        'description': 'This is the detailed description of the campaign.',
        'motivation': 'The motivation behind this campaign.',
        'type': 'Type of Charity',  # Replace with actual type
        'website': 'https://example.com',
        'start_datetime': timezone.now(),
        'end_datetime': timezone.now() + timedelta(days=30),
        'place': 'Example Location',
        'active': True,
    }

    VALID_FAQ_DATA_1 = {
        'question': 'Question 1',
        'answer': 'The purpose is to...',
        'important': 'Important information about the question.',
    }
    VALID_FAQ_DATA_2 = {
        'question': 'Question 2',
        'answer': 'The purpose is to...',
        'important': 'Important information about the question.',
    }

    def setUp(self):
        self.campaign1 = CharityCause.objects.create(**self.VALID_CHARITY_CAUSE_DATA_1)
        self.campaign2 = CharityCause.objects.create(**self.VALID_CHARITY_CAUSE_DATA_2)

        self.q_and_a1 = FAQ.objects.create(**self.VALID_FAQ_DATA_1)
        self.q_and_a2 = FAQ.objects.create(**self.VALID_FAQ_DATA_2)

        self.q_and_a1.campaigns.set([self.campaign1])
        self.q_and_a2.campaigns.set([self.campaign2])

    def test_get_unique_q_and_a(self):
        campaigns = [self.campaign1, self.campaign2]
        unique_q_and_a = CharityCausesView.get_unique_q_and_a(campaigns)
        self.assertIn(self.q_and_a1, unique_q_and_a)
        self.assertIn(self.q_and_a2, unique_q_and_a)
