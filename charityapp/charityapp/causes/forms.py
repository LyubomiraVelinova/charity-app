from django import forms

from charityapp.causes.models import SponsorDonation


class SponsorDonationForm(forms.ModelForm):
    class Meta:
        model = SponsorDonation
        fields = ['amount']
