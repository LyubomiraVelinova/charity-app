from django import forms

from charityapp.causes.models import ParticipationDonationCause


class ParticipationDonationCauseForm(forms.ModelForm):
    class Meta:
        model = ParticipationDonationCause
        fields = ['amount']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None or amount <= 0:
            raise forms.ValidationError("Please enter a valid positive amount.")
        return amount
