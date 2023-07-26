from enum import Enum

from django.core import validators
from django.db import models

from charityapp.common.mixins import ChoicesStringsMixin
from charityapp.common.validators import validate_card_verification_value, validate_card_number


def format_card_number(value):
    return ' '.join(value[i:i + 4] for i in range(0, len(value), 4))


class Amount(ChoicesStringsMixin, Enum):
    BGN_10 = '10 BGN'
    BGN_20 = '20 BGN'
    BGN_50 = '50 BGN'
    BGN_100 = '100 BGN'
    BGN_200 = '200 BGN'
    BGN_OTHER = 'Other'


class Country(ChoicesStringsMixin, Enum):
    COUNTRY = 'Bulgaria'


class PaymentMethods(ChoicesStringsMixin, Enum):
    CREDIT_CARD = 'Credit card'


class Months(ChoicesStringsMixin, Enum):
    JANUARY = '1'
    FEBRUARY = '2'
    MARCH = '3'
    APRIL = '4'
    MAY = '5'
    JUNE = '6'
    JULY = '7'
    AUGUST = '8'
    SEPTEMBER = '9'
    OCTOBER = '10'
    NOVEMBER = '11'
    DECEMBER = '12'


class Years(ChoicesStringsMixin, Enum):
    YEAR_23 = '23'
    YEAR_24 = '24'
    YEAR_25 = '25'
    YEAR_26 = '26'
    YEAR_27 = '27'
    YEAR_28 = '28'
    YEAR_29 = '29'
    YEAR_30 = '30'
    YEAR_31 = '31'
    YEAR_32 = '32'


class AboutUsInfo(models.Model):
    MAX_LENGTH_HEADER = 200

    header = models.CharField(
        max_length=MAX_LENGTH_HEADER,
    )
    description = models.TextField()
    last_updated = models.DateTimeField(
        auto_now=True,
    )


class Donation(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30
    MAX_LEN_CITY = 100
    MAX_LEN_CARD_NUMBER = 19
    MAX_LEN_CARD_VERIFICATION_VALUE = 3

    # DONATION VALUE
    donation_amount = models.CharField(
        max_length=Amount.max_length(),
        choices=Amount.choices(),
    )

    # CONTACT INFORMATION
    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField()

    phone_number = models.IntegerField(
        null=False,
        blank=False,
    )

    # BILLING INFORMATION
    country = models.CharField(
        choices=Country.choices(),
        null=False,
        blank=False,
    )
    city = models.CharField(
        max_length=MAX_LEN_CITY,
        null=False,
        blank=False,
    )
    postal_code = models.CharField(
        max_length=MAX_LEN_CITY,
        null=False,
        blank=False,
    )
    address = models.CharField(
        max_length=MAX_LEN_CITY,
        null=False,
        blank=False,
    )

    # PAYMENT METHOD
    payment_method = models.CharField(
        choices=PaymentMethods.choices(),
        null=False,
        blank=False,
    )
    holder_name = models.CharField()

    card_verification_value = models.CharField(
        max_length=MAX_LEN_CARD_VERIFICATION_VALUE,
        validators=[validate_card_verification_value],
        help_text='Enter the three-digit card verification value (CVV/CVC) from the back of your card.',
        null=False,
        blank=False,
    )
    card_number = models.CharField(
        max_length=MAX_LEN_CARD_NUMBER,
        validators=[validate_card_number],
        help_text='Enter the three-digit card verification value (CVV/CVC) from the back of your card.',
        null=False,
        blank=False,
    )

    card_expiration_month = models.CharField(
        max_length=Months.max_length(),
        choices=Months.choices(),
        null=False,
        blank=False,
    )

    card_expiration_year = models.CharField(
        max_length=Years.max_length(),
        choices=Years.choices(),
        null=False,
        blank=False,
    )

    def save(self, *args, **kwargs):
        self.card_number = format_card_number(self.card_number.replace(' ', ''))
        super(Donation, self).save(*args, **kwargs)
