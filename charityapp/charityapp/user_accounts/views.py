from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from django.contrib.auth import mixins as auth_mixins

from charityapp.user_accounts.forms import RegisterUserForm, AuthenticationUserForm, ChangeEmailUserForm
from charityapp.user_profiles.models import SponsorProfile, MemberProfile, VolunteerProfile

UserModel = get_user_model()


# VERIFICATION
# from allauth.account.utils import complete_signup
# from allauth.account import views as accounts_view


# REGSITER AND AUTHENTICATION - NOT WORKING
# class RegisterUserView(accounts_view.SignupView):
#     template_name = 'user_accounts/register-page.html'
#     form_class = RegisterUserForm
#     success_url = reverse_lazy('profile-edit')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['register_form'] = self.get_form()
#         return context
#
#     def form_valid(self, form):
#         user = form.save(self.request)
#         response = complete_signup(
#             self.request,
#             user,
#             self.get_success_url(),
#             None,
#         )
#         login(self.request, user)
#         return response


class RegisterUserView(views.CreateView):
    template_name = 'user_accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile-edit-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)

        # Create related profile based on user_type
        user_type = form.cleaned_data.get('user_type')
        if user_type == "SPONSOR":
            SponsorProfile.objects.create(user=user)
        elif user_type == "MEMBER":
            MemberProfile.objects.create(user=user)
        elif user_type == "VOLUNTEER":
            VolunteerProfile.objects.create(user=user)

        subject = 'Welcome'
        context = {'user': user}
        message = render_to_string('user_accounts/registration-email-greeting.html', context)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, html_message=message)

        return response


class LoginUserView(auth_views.LoginView):
    template_name = 'user_accounts/login-page.html'
    form_class = AuthenticationUserForm


class PasswordChangeUserView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = "user_accounts/password-change-page.html"
    success_url = reverse_lazy("password-change-done-page")


class PasswordChangeDoneUserView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = "user_accounts/password-change-done.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        logout(self.request)
        return response


class EmailChangeUserView(auth_mixins.LoginRequiredMixin, views.FormView):
    template_name = 'user_accounts/email-change-page.html'
    form_class = ChangeEmailUserForm
    success_url = reverse_lazy('email-change-done-page')

    def form_valid(self, form):
        new_email = form.cleaned_data['new_email']
        confirm_email = form.cleaned_data['confirm_email']
        if new_email == confirm_email:
            self.request.user.email = new_email
            self.request.user.save()
            return redirect(self.get_success_url())
        else:
            form.add_error('confirm_email', 'Email addresses do not match.')
            return self.form_invalid(form)


class EmailChangeDoneUserView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = "user_accounts/email-change-done.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        logout(self.request)
        return response
