from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from charityapp.charity.forms import TestimonialForm
from charityapp.user_profiles.models import VolunteerProfile, SponsorProfile, MemberProfile


@login_required
@user_passes_test(lambda user: user.user_type in ['VOLUNTEER', 'SPONSOR', 'MEMBER'])
def testimonial_submission(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user

            # user_type = request.user.user_type
            # if user_type == 'VOLUNTEER':
            #     try:
            #         volunteer_profile = VolunteerProfile.objects.get(user=request.user)
            #         testimonial.name = volunteer_profile.full_name
            #         testimonial.picture = volunteer_profile.profile_picture
            #     except VolunteerProfile.DoesNotExist:
            #         pass
            # elif user_type == 'SPONSOR':
            #     try:
            #         sponsor_profile = SponsorProfile.objects.get(user=request.user)
            #         testimonial.name = sponsor_profile.company_name
            #         testimonial.picture = sponsor_profile.logo
            #     except SponsorProfile.DoesNotExist:
            #         pass
            # elif user_type == 'MEMBER':
            #     try:
            #         member_profile = MemberProfile.objects.get(user=request.user)
            #         testimonial.name = member_profile.full_name
            #         testimonial.picture = member_profile.profile_picture
            #     except MemberProfile.DoesNotExist:
            #         pass

            testimonial.save()
            return redirect('homepage')  # Redirect to the homepage after successful submission
    else:
        form = TestimonialForm()
    return render(request, 'charity/testimonial-submission-page.html', {'form': form})
