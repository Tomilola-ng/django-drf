""" User Account Model """

import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserAccountManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """Define a model for UserAccount."""

    ROLE_CHOICES = (
        ('default', 'Default'),
        ('admin', 'Admin'),
    )

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name=_(
        "Email Address"), max_length=255, unique=True, db_index=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,
                            default='default', db_index=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        """Define Meta options for UserAccount."""
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_short_name(self):
        """ Return the short name for the user. """
        return self.first_name

    def __str__(self):
        return f"{self.email}"
