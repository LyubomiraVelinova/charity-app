from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth import mixins as auth_mixins

from charityapp.user_accounts.forms import RegisterUserForm, CustomAuthenticationForm, ChangeEmailForm


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
#             None,  # Тук премахваме извикването на get_redirect_url
#         )
#         login(self.request, user)  # Извършваме логин на потребителя
#         return response


class RegisterUserView(views.CreateView):
    template_name = 'user_accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('profile-edit')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.get_form()
        return context

    def form_valid(self, form):
        # This will create the user
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)

        # Send a greeting email to the user using the email template
        subject = 'Welcome'
        context = {'user': user}
        message = render_to_string('confirmation/emails/email-greeting.html', context)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, html_message=message)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'user_accounts/login-page.html'
    form_class = CustomAuthenticationForm


class LogoutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    pass


class CustomPasswordChangeView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = "user_accounts/password-change-page.html"
    success_url = reverse_lazy("change-password-done")


class CustomPasswordChangeDoneView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = "user_accounts/password-change-done-page.html"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        logout(self.request)
        return response

    
class ChangeEmailView(auth_mixins.LoginRequiredMixin, views.FormView):
    template_name = 'user_accounts/change_email.html'
    form_class = ChangeEmailForm
    success_url = reverse_lazy('profile-details')  # Redirect to the user's profile page after successful email change

    def form_valid(self, form):
        new_email = form.cleaned_data['new_email']
        confirm_email = form.cleaned_data['confirm_email']
        if new_email == confirm_email:
            # Update the user's email address
            self.request.user.email = new_email
            self.request.user.save()
            return redirect(self.get_success_url())
        else:
            form.add_error('confirm_email', 'Email addresses do not match.')
            return self.form_invalid(form)
