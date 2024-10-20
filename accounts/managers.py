""" User Account Manager """

from django.contrib.auth.models import BaseUserManager


class UserAccountManager(BaseUserManager):
    """Define a model manager for UserAccount."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """Create and save a SuperUser with the given email and password."""
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_active') is not True:
            raise ValueError('Super User must be active')
        if kwargs.get('is_staff') is not True:
            raise ValueError('Super User must be staff')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Super User must have is superuser is True')

        return self.create_user(email, password, **kwargs)
