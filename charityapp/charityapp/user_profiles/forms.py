from django import forms

from charityapp.user_profiles.models import VolunteerProfile, MemberProfile, SponsorProfile, Testimonial


class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('first_name', 'last_name', 'gender', 'phone_number', 'bio', 'interests', 'profile_picture',)


class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = (
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'strengths',
            'interests',
            'role',
            'profile_picture',
        )


class SponsorProfileForm(forms.ModelForm):
    class Meta:
        model = SponsorProfile
        fields = ('company_name', 'logo', 'website', 'career_field')


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['quote', 'allow_posting']

    allow_posting = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='I allow "Club for Future" to publish my testimonial on this website.',
    )
