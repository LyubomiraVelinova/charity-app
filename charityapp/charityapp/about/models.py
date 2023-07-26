from django.db import models

from django.core import validators


class People(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30
    MAX_LEN_ROLE = 100

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME),
        ),
        # Required field
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

    member_role = models.CharField(
        max_length=MAX_LEN_ROLE,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_first_three_sentences(self):
        sentences = self.description.split('.')
        first_three = '.'.join(sentences[:3])
        return first_three


class MissionAndValues(models.Model):
    pass


class History(models.Model):
    pass