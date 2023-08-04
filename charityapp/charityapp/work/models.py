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
    MAX_LEN_PLACE = 200

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )
    resume = models.TextField(
        null=False,
        blank=False,
    )
    image = models.ImageField()
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
    start_datetime = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
    )
    end_datetime = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
    )
    place = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    # Начини за участие и подкрепа: Предоставете информация за начините, по които хората могат да се включат в кампанията или да я подкрепят. Това може да бъде чрез дарение, участие в събитието, спонсорство и други.
    #
    # Истории за успех: Ако имате предишни успешни кампании или проекти, споделете истории за тях и как те са помогнали на общността или хората, които са били засегнати.
    # Мога да направя релация с testimonials,в testimonials да има опция да си избереш кампанията, в която си участвал и тук да се появяват някакви коментари на доброволци, ако са участвали по съответната кампания.

    def duration(self):
        return f'{self.start_datetime} - {self.end_datetime}'

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

    def __str__(self):
        return self.title


class FAQCampaigns(models.Model):
    MAX_LEN_QUESTION = 200

    campaigns = models.ManyToManyField(CharityCampaigns, related_name='q_and_a')

    question = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    answer = models.TextField(
        null=False,
        blank=False,
    )

    important = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.question}'
