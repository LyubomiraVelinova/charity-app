from django import forms

from charityapp.common.models import AboutUsInfo, Donation


class AboutUsInfoForm(forms.ModelForm):
    class Meta:
        model = AboutUsInfo
        fields = ['header', 'description']


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'


class DonationValueForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('donation_amount',)


class DonationContactInfoForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class DonationBillingInfoForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('country', 'city', 'postal_code', 'address')


class DonationPaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('payment_method', 'holder_name', 'card_verification_value', 'card_number', 'card_expiration_month',
                  'card_expiration_year')
