from django.core.exceptions import ValidationError
from django.test import TestCase

from charityapp.causes.models import DonationCause
from charityapp.common.models import Donation


class DonationTests(TestCase):
    VALID_DONATION_DATA = {
        'donation_amount': '50 BGN',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'phone_number': '0888123456',
        'country': 'Bulgaria',
        'city': 'Sofia',
        'postal_code': '1000',
        'address': '123 Main St',
        'payment_method': 'Test card',
        'holder_name': 'John Doe',
        'card_verification_value': '123',
        'card_number': '4111111111111111',
        'card_expiration_month': '9',
        'card_expiration_year': '28',
    }

    VALID_DONATION_CAMPAIGN_DATA = {
        'title': 'Example Cause',
        'description': 'This is an example cause description.',
        'purpose': 'The purpose of this cause is to support a local charity.',
        'goal_amount': 1000.00,
        'current_amount': 500.00,
        'start_date': '2023-08-01',
        'end_date': '2023-08-31',
        'succeeded': False,
    }

    def test_create__when_valid__expect_to_be_created(self):
        donation = Donation.objects.create(**self.VALID_DONATION_DATA)
        self.assertIsNotNone(donation.pk)

    def test_create__when_phone_is_none_expect_to_raise(self):
        invalid_data = {
            'phone_number': None,
        }
        donation_data = {**self.VALID_DONATION_DATA, **invalid_data}

        with self.assertRaises(ValidationError):
            donation = Donation.objects.create(**donation_data)
            # Needed explicit call in tests
            donation.full_clean()

    def test_create__when_phone_not_starts_with_0_plus__expect_to_raise(self):
        invalid_data = {
            'phone_number': '878778898',
        }
        donation_data = {**self.VALID_DONATION_DATA, **invalid_data}

        with self.assertRaises(ValidationError):
            donation = Donation.objects.create(**donation_data)
            # Needed explicit call in tests
            donation.full_clean()

    def test_create__when_card_verification_value_less_than_three_digits__expected_to_raise(self):
        invalid_data = {
            'card_verification_value': '56',
        }
        donation_data = {**self.VALID_DONATION_DATA, **invalid_data}

        with self.assertRaises(ValidationError):
            donation = Donation.objects.create(**donation_data)
            donation.full_clean()

    def test_create_when_card_verification_value_non_digit__expected_to_raise(self):
        invalid_data = {
            'card_verification_value': '64f',
        }
        donation_data = {**self.VALID_DONATION_DATA, **invalid_data}

        with self.assertRaises(ValidationError):
            donation = Donation.objects.create(**donation_data)
            donation.full_clean()

    def test_save_method__when_valid_card_number__expect_to_be_formatted(self):
        formatted_data = {
            'card_number': '2222888899996666',
        }
        donation_data = {**self.VALID_DONATION_DATA, **formatted_data}
        donation = Donation(**donation_data)
        donation.save()
        self.assertEqual(donation.card_number, '2222 8888 9999 6666')

    def test_distribute_amount_to_campaigns_when_donation_is_done_expect_to_be_distributed(self):
        value_data = {
            'donation_amount': '100',
        }
        donation_campaign_amount_data = {
            'goal_amount': 2000.00,
            'current_amount': 200.00,
        }

        first_campaign = DonationCause.objects.create(**self.VALID_DONATION_CAMPAIGN_DATA)
        second_campaign = DonationCause.objects.create(
            **{**self.VALID_DONATION_CAMPAIGN_DATA,
               **donation_campaign_amount_data}
        )

        donation_data = {**self.VALID_DONATION_DATA, **value_data}
        donation = Donation.objects.create(**donation_data)
        donation.distribute_amount_to_campaigns()

        first_campaign.refresh_from_db()
        second_campaign.refresh_from_db()

        self.assertEqual(first_campaign.current_amount, 550)
        self.assertEqual(second_campaign.current_amount, 250)
