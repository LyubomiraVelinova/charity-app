from django.db import models

from charityapp.accounts.models import AppUser


class Blog(models.Model):
    title = models.CharField(
        max_length=100
    )
    introduction = models.TextField()
    content = models.TextField()
    conclusion = models.TextField()
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    featured_image = models.ImageField(
        upload_to='static/images/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
