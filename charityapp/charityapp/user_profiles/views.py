from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from charityapp.accounts.models import AppUser
from charityapp.user_profiles.forms import VolunteerForm, SponsorForm, MemberForm
from charityapp.user_profiles.models import VolunteerProfile, SponsorProfile, MemberProfile

UserModel = get_user_model()


class ProfileEditView(views.UpdateView):
    template_name = 'user_profiles/profile-edit-page.html'
    success_url = reverse_lazy('profile-details-page')

    def get_form_class(self):
        user_type = self.request.user.user_type
        if user_type == 'VOLUNTEER':
            return VolunteerForm
        elif user_type == 'SPONSOR':
            return SponsorForm
        elif user_type == 'MEMBER':
            return MemberForm

    def get_object(self, queryset=None):
        user = self.request.user
        if user.user_type == 'VOLUNTEER':
            return user.volunteer_profile
        elif user.user_type == 'SPONSOR':
            return user.sponsor_profile
        elif user.user_type == 'MEMBER':
            return user.member_profile

    def form_valid(self, form):
        user_type = self.request.user.user_type
        form.instance.user = self.request.user  # Задаване на текущия потребител
        return super().form_valid(form)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_object = self.get_object()
        current_model = user_object._meta.model
        excluded_fields = ["user", "first_name", "last_name", "company_name", "profile_picture", "logo",
                           "charity_history", "donation_history"]
        fields = [f.name for f in current_model._meta.get_fields() if f.name not in excluded_fields]

        context['fields'] = fields
        return context


class ProfileDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'user_profiles/profile-edit-page.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return redirect(self.get_success_url())


# NOT WORKING
class ChangePhotoView(views.UpdateView):
    model = UserModel
    template_name = 'user_profiles/profile-edit-page.html'
    fields = ['profile_photo', 'logo']
    success_url = reverse_lazy('profile-edit-page')

    def get_object(self, queryset=None):
        return self.request.user


class SecuritySettingsView(views.TemplateView):
    template_name = 'user_profiles/security-settings-page.html'


class VolunteerListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'user_profiles/volunteers-list-page.html'
