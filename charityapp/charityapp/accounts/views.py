from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from django.contrib.auth import mixins as auth_mixins

from charityapp.accounts.forms import RegisterUserForm, CustomAuthenticationForm, ChangeEmailForm


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
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
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = CustomAuthenticationForm


class LogoutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    pass


class CustomPasswordChangeView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = "accounts/password-change-page.html"
    success_url = reverse_lazy("change-password-done")


class CustomPasswordChangeDoneView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = "accounts/"


class ChangeEmailView(auth_mixins.LoginRequiredMixin, views.FormView):
    template_name = 'accounts/change_email.html'
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


