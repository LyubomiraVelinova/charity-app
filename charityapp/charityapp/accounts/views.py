from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from charityapp.accounts.forms import RegisterUserForm, CustomAuthenticationForm
from charityapp.user_profiles.forms import VolunteerForm, SponsorForm, MemberForm

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from charityapp.accounts.forms import RegisterUserForm, CustomAuthenticationForm
from charityapp.accounts.models import UserType


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form()
        return context

    def form_valid(self, form):
        # This will create the user
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


class AdditionalRegisterUserView(views.CreateView):
    template_name = 'accounts/additional-register-page.html'
    success_url = reverse_lazy('home-page')
    form_class = None

    def get_form_class(self):
        user_type = self.kwargs['user_type']
        if user_type == 'VOLUNTEER':
            return VolunteerForm
        elif user_type == 'SPONSOR':
            return SponsorForm
        elif user_type == 'MEMBER':
            return MemberForm
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_type = self.kwargs.get('user_type')

        context['user_type'] = user_type
        context['form'] = self.get_form_class()
        return context

    def form_valid(self, form):
        user_type = self.kwargs['user_type']
        form.instance.user = self.request.user  # Задаване на текущия потребител
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = CustomAuthenticationForm


class LogoutView(auth_views.LogoutView):
    pass
