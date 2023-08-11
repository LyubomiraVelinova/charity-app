from django.core.exceptions import ValidationError
from django.db import models

from charityapp.user_accounts.models import AppUser


class Article(models.Model):
    MAX_LEN_TITLE = 100

    title = models.CharField(
        max_length=MAX_LEN_TITLE
    )

    subtitle = models.CharField(
        max_length=MAX_LEN_TITLE
    )

    short_resume = models.TextField()
    introduction = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    featured_image = models.URLField(
        # upload_to='static/images/',
        null=True,
        blank=True,
    )

    def clean(self):
        if len(self.short_resume) > 150:
            raise ValidationError({'short_resume': 'Short resume cannot exceed 150 characters.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Run model validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.subtitle}'
