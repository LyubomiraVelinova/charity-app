from django import forms

from charityapp.common.models import AboutUsInfo, RandomUserDonation


class AboutUsInfoForm(forms.ModelForm):
    class Meta:
        model = AboutUsInfo
        fields = ['header', 'description']


class DonationForm(forms.ModelForm):
    class Meta:
        model = RandomUserDonation
        fields = '__all__'


class DonationValueForm(forms.ModelForm):
    class Meta:
        model = RandomUserDonation
        fields = ('donation_amount',)


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = RandomUserDonation
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class BillingInfoForm(forms.ModelForm):
    class Meta:
        model = RandomUserDonation
        fields = ('country', 'city', 'postal_code', 'address')


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = RandomUserDonation
        fields = ('payment_method', 'holder_name', 'card_verification_value', 'card_number', 'card_expiration_month',
                  'card_expiration_year')
