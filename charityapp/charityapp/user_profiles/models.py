from enum import Enum

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils import timezone

from charityapp.accounts.models import AppUser
from charityapp.common.mixins import ChoicesStringsMixin
from charityapp.work.models import DonationCampaign, CharityCampaign


class Gender(ChoicesStringsMixin, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'


# class CareerFields(ChoicesStringsMixin, Enum):
#     ARCHITECTURE_AND_CONSTRUCTION = "ARCHITECTURE AND CONSTRUCTION"
#     ACCOUNTING_BANKING_AND_FINANCE = "ACCOUNTING, BANKING AND FINANCE"
#     AGRICULTURE_FARMING_AND_FOOD = "AGRICULTURE, FARMING AND FOOD"
#     ARTS_CULTURE_AND_ENTERTAINMENT = "ARTS, CULTURE AND ENTERTAINMENT"
#     BUSINESS_MANAGEMENT_AND_ADMINISTRATION = "BUSINESS, MANAGEMENT AND ADMINISTRATION"
#     COMMUNICATIONS = "COMMUNICATIONS"
#     COMPUTER_TECHNOLOGY = "COMPUTER TECHNOLOGY"
#     CUSTOMER_SERVICE_AND_SALES = "CUSTOMER SERVICE AND SALES"
#     EDUCATION_AND_TRAINING = "EDUCATION AND TRAINING"
#     ENVIRONMENT = "ENVIRONMENT"
#     GOVERNMENT_AND_MILITARY = "GOVERNMENT AND MILITARY"
#     HEALTH_AND_MEDICAL = "HEALTH AND MEDICAL"
#     HOSPITALITY_TRAVEL_AND_TOURISM = "HOSPITALITY, TRAVEL AND TOURISM"
#     INSTALLATION_MAINTENANCE_AND_REPAIR = "INSTALLATION, MAINTENANCE AND REPAIR"
#     LAW_PUBLIC_POLICY_ENFORCEMENT_AND_SAFETY = "LAW, PUBLIC POLICY, ENFORCEMENT AND SAFETY"
#     MANUFACTURING_AND_PRODUCTION = "MANUFACTURING AND PRODUCTION"
#     MEDIA_AND_BROADCAST = "MEDIA AND BROADCAST"
#     STEM = "STEM"
#     SOCIAL_CHARITY_AND_COMMUNITY_SERVICE = "SOCIAL, CHARITY AND COMMUNITY SERVICE"
#     TRANSPORT_AND_DISTRIBUTION = "TRANSPORT AND DISTRIBUTION"
#     OTHER = "OTHER"


UserModel = get_user_model()


class SponsorProfile(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 100
    MAX_LEN_CAREER = 100

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='sponsor_profile',
        primary_key=True,
    )

    company_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        verbose_name='Company name',
    )

    logo = models.ImageField(
        null=True,
        blank=True,
    )

    website = models.URLField(
        verbose_name='Website',
    )

    career_field = models.CharField(
        max_length=MAX_LEN_CAREER,
        null=True,
        blank=True,
        verbose_name='Career field',
    )
    donation_history = models.ManyToManyField(
        DonationCampaign,
        verbose_name='Donation history',
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Sponsor Profile'
        verbose_name_plural = 'Sponsors Profile'


class CharityInterests(ChoicesStringsMixin, Enum):
    ENVIRONMENTAL_CAUSES = "Environmental causes"
    HUMANITARIAN_CAUSES = "Humanitarian causes"
    DISASTERS_AND_ACCIDENTS_CAUSES = "Causes of disasters and accidents"
    ANIMAL_CAUSES = "Animal causes"
    OTHER = "Other"


class VolunteerProfile(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='volunteer_profile',
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
        verbose_name='First name',
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
        verbose_name='Last name',
    )

    gender = models.CharField(
        max_length=MAX_LEN_NAME,
        choices=Gender.choices(),
        default=Gender.DO_NOT_SHOW,
        verbose_name='Gender',
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        null=True,
        blank=True,
        verbose_name='Phone number',
    )

    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='About',
    )

    interests = models.CharField(
        max_length=CharityInterests.max_length(),
        choices=CharityInterests.choices(),
        verbose_name='Charity interests',
    )

    charity_history = models.ManyToManyField(
        CharityCampaign,
        verbose_name='Charity history',
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Volunteer Profile'
        verbose_name_plural = 'Volunteers Profile'


class RoleTypes(ChoicesStringsMixin, Enum):
    CHAIRMAN = "Chairman"
    VICE_CHAIRMAN = "Vice Chairman"
    SECRETARY = "Secretary"
    ADMINISTRATOR = "Administrator"
    MODERATOR = "Moderator"
    CASHIER = "Cashier"
    PR = "PR"
    OTHER = "Other"


class MemberProfile(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30
    MAX_LENGTH_INTERESTS = 50
    MAX_LENGTH_ROLE = 50

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='member_profile',
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
        verbose_name='First name',
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        null=False,
        blank=False,
        verbose_name='Last name',
    )

    gender = models.CharField(
        max_length=MAX_LEN_NAME,
        choices=Gender.choices(),
        default=Gender.DO_NOT_SHOW,
        verbose_name='Gender',
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        null=True,
        blank=True,
        verbose_name='Phone number',
    )

    strengths = models.TextField(
        null=True,
        blank=True,
        verbose_name='Strengths',
    )

    interests = models.CharField(
        max_length=CharityInterests.max_length(),
        choices=CharityInterests.choices(),
        verbose_name='Charity interests',
    )

    role = models.CharField(
        max_length=RoleTypes.max_length(),
        choices=RoleTypes.choices(),
        verbose_name='Role in the club',
    )

    charity_history = models.ManyToManyField(
        CharityCampaign,
        verbose_name='Charity history',
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Member Profile'
        verbose_name_plural = 'Members Profile'
