""" User Account Forms """

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserAccount


class CustomUserCreationForm(UserCreationForm):
    """Define a form for creating UserAccount."""
    class Meta(UserCreationForm):
        """Define Meta options for CustomUserCreationForm."""
        model = UserAccount
        fields = ["email",  "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    """Define a form for updating UserAccount."""
    class Meta:
        """Define Meta options for CustomUserChangeForm."""
        model = UserAccount
        fields = ["email",  "first_name", "last_name"]
        error_class = "error"
