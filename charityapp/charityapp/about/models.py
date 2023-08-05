from django.db import models

from django.core import validators


class Person(models.Model):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30
    MAX_LEN_ROLE = 100

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

    member_role = models.CharField(
        max_length=MAX_LEN_ROLE,
    )

    profile_picture = models.URLField(
        null=False,
        blank=False,
        default='static/images/anonymous_profile.jpg',
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_first_twenty_words(self):
        sentences = self.description.split(' ')
        first_thirty_words = ' '.join(sentences[:20])
        return first_thirty_words

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Our People'


class Timeline(models.Model):
    MAX_LEN_TITLE = 100

    event_date = models.DateField(
        null=False,
        blank=False,
    )
    event_title = models.CharField(
        max_length=MAX_LEN_TITLE,
        null=False,
        blank=False,
    )
    event_summary = models.TextField(
        null=False,
        blank=False,
    )
    event_image = models.URLField(
        null=True,
        blank=True,
    )

    def get_first_fifty_words(self):
        words = self.event_summary.split(' ')
        first_fifty_words = ' '.join(words[:50])
        return first_fifty_words

    class Meta:
        verbose_name = 'Timeline Data'
        verbose_name_plural = 'Timeline Data'
