from django.db import models

from charityapp.accounts.models import AppUser


class Testimonial(models.Model):
    quote = models.TextField()
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
