from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser, User
from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm
from shop.models import CustomUser


# class CustomUser(AbstractUser):
#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[AbstractUser.username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#         null=True,
#         blank=True,
#     )
#
#     email = models.EmailField(_("email address"), unique=True, )
#
#     is_active = models.BooleanField(
#         _("active"),
#         default=True,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#

class BaseRegisterForm(CustomUserCreationForm):

    class Meta:
        # model = User
        model = CustomUser
        fields = (#"username",
                  # "first_name",
                  # "last_name",
                  "email",
                  "password1",
                  "password2",
                  )