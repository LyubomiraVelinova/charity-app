from django import forms

from charityapp.user_profiles.models import VolunteerProfile, MemberProfile, SponsorProfile


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('first_name', 'last_name', 'gender', 'phone_number', 'bio', 'interests', 'profile_picture')


class MemberForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ('first_name', 'last_name', 'gender', 'phone_number', 'strengths', 'interests', 'role', 'profile_picture')


class SponsorForm(forms.ModelForm):
    class Meta:
        model = SponsorProfile
        fields = ('company_name', 'logo', 'website', 'career_field')
