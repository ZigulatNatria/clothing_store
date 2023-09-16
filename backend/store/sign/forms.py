from django import forms
from django.contrib.auth import password_validation
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
                    "autofocus": True,
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Email',
                }))
    password = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                    "autocomplete": "current-password",
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Пароль',
                }))


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                    "autocomplete": "current-password",
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Пароль',
                }),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                    "autocomplete": "current-password",
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Повторите пароль',
                }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        "class": "form-control",
        "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
        "placeholder": 'Email',
    }))

    # email = forms.EmailField(
    #     label=_("Email"),
    #     max_length=254,
    #     widget=forms.EmailInput(attrs={
    #         "autocomplete": "email",
    #         "class": "form-control",
    #         "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
    #         "placeholder": 'Email',
    # }))
