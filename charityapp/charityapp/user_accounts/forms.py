from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please."),
    )

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     try:
    #         validate_email(email)
    #     except ValidationError:
    #         raise forms.ValidationError('Please enter a valid email address.')
    #     if UserModel.objects.filter(email=email).exists():
    #         raise forms.ValidationError('This email is already in use.')
    #     return email

    class Meta:
        model = UserModel
        fields = ('email', 'user_type', 'password1', 'password2')


class CustomAuthenticationForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'EMAIL'
        self.fields['password'].widget.attrs['placeholder'] = 'PASSWORD'


class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(label='New Email Address')
    confirm_email = forms.EmailField(label='Confirm New Email Address')
