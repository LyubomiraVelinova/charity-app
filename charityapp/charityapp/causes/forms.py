from django import forms

from charityapp.causes.models import ParticipationDonationCause


class ParticipationDonationCauseForm(forms.ModelForm):
    class Meta:
        model = ParticipationDonationCause
        fields = ['amount']
