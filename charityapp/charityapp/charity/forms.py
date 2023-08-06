from django import forms

from charityapp.charity.models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['quote', 'allow_posting']

    allow_posting = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='I allow "Club for Future" to publish my testimonial on this website.',
    )
