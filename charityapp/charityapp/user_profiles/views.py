from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from charityapp.accounts.models import UserType
from charityapp.user_profiles.forms import VolunteerForm, SponsorForm, MemberForm
from charityapp.user_profiles.models import VolunteerProfile, SponsorProfile, MemberProfile

UserModel = get_user_model()


# class ProfileEditView(views.UpdateView):
#     template_name = 'user_profiles/profile-edit-page.html'


def profile_edit_view(request):
    user_type = request.user.user_type
    user = request.user

    if request.method == 'POST':
        if user_type == 'VOLUNTEER':
            form = VolunteerForm(request.POST, instance=user.volunteer_profile)
            if form.is_valid():
                form.save()
                return redirect('home-page')
        elif user_type == 'SPONSOR':
            form = SponsorForm(request.POST, instance=user.sponsor_profile)
            if form.is_valid():
                form.save()
                return redirect('home-page')
        elif user_type == 'MEMBER':
            form = MemberForm(request.POST, instance=user.member_profile)

        if form.is_valid():
            form.save()
            return redirect('home-page')

    elif request.method == 'GET':
        if user_type == 'VOLUNTEER':
            form = VolunteerForm(instance=user.volunteer_profile)
        elif user_type == 'SPONSOR':
            form = SponsorForm(instance=user.sponsor_profile)
        elif user_type == 'MEMBER':
            form = MemberForm(instance=user.member_profile)

    context = {
        'user': user,
        'user_type': user_type,
        'form': form,
    }

    return render(request, 'user_profiles/profile-edit-page.html', context)


class ProfileDetailsView(views.DetailView):
    template_name = 'user_profiles/profile-details-page.html'

    def get_object(self, queryset=None):
        user_type = self.request.user.user_type
        if user_type == 'VOLUNTEER':
            return VolunteerProfile.objects.get(user=self.request.user)
        elif user_type == 'SPONSOR':
            return SponsorProfile.objects.get(user=self.request.user)
        elif user_type == 'MEMBER':
            return MemberProfile.objects.get(user=self.request.user)


class ProfileDeleteView(views.DeleteView):
    template_name = 'user_profiles/profile-delete-page.html'


class VolunteerListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'user_profiles/volunteers-list-page.html'

# DO I REALLY NEED THIS??? AND THIS TEMPLATES???
# @login_required
# def sponsor_profile(request, sponsor_id):
#     context = {
#         'sponsor': get_object_or_404(SponsorsProfiles, pk=sponsor_id),
#     }
#     return render(request, 'sponsor-profile-page.html', context)
#
#
# @login_required
# def benefactor_profile(request, benefactor_id):
#     context = {
#         'benefactor': get_object_or_404(BenefactorsProfiles, pk=benefactor_id)
#     }
#     return render(request, 'benefactor-profile-page.html', context)
#
# @login_required
# def helper_profile(request, helper_id):
#     context = {
#         'helper': get_object_or_404(HelperProfiles, pk=helper_id)
#     }
#     return render(request, 'helper-profile-page.html', context)
