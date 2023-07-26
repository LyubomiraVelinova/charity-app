from enum import Enum

from django.db import models
from django.utils import timezone

from charityapp.common.mixins import ChoicesStringsMixin


class CharityType(ChoicesStringsMixin, Enum):
    ENVIRONMENTAL_CHARITY = "Environmental Charity"
    CHILDRENS_CHARITY = "Children’s Charity"
    HUMAN_RIGHTS_CHARITY = "Human Rights Charity"
    DISASTER_RELIEF_CHARITY = "Disaster Relief Charity"
    SCIENTIFIC_RESEARCH_CHARITY = "Scientific Research Charity"
    SENIOR_CITIZEN_CHARITY = "Senior Citizen Charity"
    CULTURAL_CHARITY = "Cultural Charity"
    ANIMAL_BASED_CHARITY = "Animal-Based Charity"
    SPORTS_BASED_CHARITY = "Sports-Based Charity"
    EDUCATION_CHARITY = "Education Charity"
    OTHER = "Other"


class CharityCampaigns(models.Model):
    MAX_LEN_NAME = 50
    MAX_LEN_TYPE = 50

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )
    resume = models.TextField(
        null=False,
        blank=False,
    )
    # NOT WORKING WITH IMAGEFIELD
    image = models.URLField()
    description = models.TextField()
    motivation = models.TextField()
    type = models.CharField(
        max_length=CharityType.max_length(),
        choices=CharityType.choices(),
    )
    # logo = models.ImageField()
    website = models.URLField(
        null=True,
        blank=True,
    )
    start_date = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
    )

    def duration(self):
        return f'{self.start_date} - {self.end_date}'

    def __str__(self):
        return self.name


class DonationCampaigns(models.Model):
    MAX_LEN_TITLE = 100

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
    )
    description = models.TextField()
    motivation = models.TextField()
    goal_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    current_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    succeeded = models.BooleanField(
        default=False,
    )

    # Many to many fields

    def __str__(self):
        return self.title

# def validate_only_alphanumeric(value):
#     for ch in value:
#         if not ch.isalnum():
#             raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
