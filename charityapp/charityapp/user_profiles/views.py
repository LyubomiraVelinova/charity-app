from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from charityapp.user_accounts.forms import RegisterUserForm
from charityapp.user_profiles.forms import VolunteerProfileForm, SponsorProfileForm, MemberProfileForm, TestimonialForm
from charityapp.user_profiles.models import VolunteerProfile, SponsorProfile, MemberProfile, Testimonial

UserModel = get_user_model()


class ProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'user_profiles/profile-edit-page.html'
    success_url = reverse_lazy('profile-details-page')

    def get_form_class(self):
        user_type = self.request.user.user_type
        if user_type == 'VOLUNTEER':
            return VolunteerProfileForm
        elif user_type == 'SPONSOR':
            return SponsorProfileForm
        elif user_type == 'MEMBER':
            return MemberProfileForm

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


class ProfileDetailsView(auth_mixins.LoginRequiredMixin,views.DetailView):
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


# CHECK THEM

class VolunteerRegisterView(views.CreateView):
    template_name = 'user_profiles/volunteer-register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile-edit-page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Скриваме полето 'user_type', за да не се показва на потребителя
        form.fields['user_type'].widget = forms.HiddenInput()
        # Задаваме предварителна стойност 'VOLUNTEER' на полето 'user_type'
        form.fields['user_type'].initial = 'VOLUNTEER'
        return form

    def form_valid(self, form):
        form.instance.user_type = 'VOLUNTEER'  # Задаваме стойност 'VOLUNTEER' за user_type
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


class SponsorRegisterView(views.CreateView):
    template_name = 'user_profiles/sponsor-register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile-edit-page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['user_type'].widget = forms.HiddenInput()
        form.fields['user_type'].initial = 'SPONSOR'
        return form

    def form_valid(self, form):
        form.instance.user_type = 'SPONSOR'
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


class MemberRegisterView(views.CreateView):
    template_name = 'user_profiles/member-register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile-edit-page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['user_type'].widget = forms.HiddenInput()
        form.fields['user_type'].initial = 'MEMBER'
        return form

    def form_valid(self, form):
        form.instance.user_type = 'MEMBER'
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


class TestimonialSubmissionView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'user_profiles/testimonial-submission-page.html'
    form_class = TestimonialForm
    success_url = reverse_lazy('testimonials-history-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TestimonialDeleteView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    template_name = 'user_profiles/testimonials-history-page.html'
    success_url = reverse_lazy('testimonials-history-page')
    model = Testimonial

    def test_func(self):
        # Check if the logged-in user is the author of the testimonial
        testimonial = self.get_object()
        return self.request.user == testimonial.author


class TestimonialsHistoryView(views.TemplateView):
    template_name = 'user_profiles/testimonials-history-page.html'
