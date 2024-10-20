""" Custom Authentication """

from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings


class CustomJWTAuthentication(JWTAuthentication):
    """Define a custom JWT Authentication."""

    def authenticate(self, request):
        """Authenticate the request."""
        try:
            header = self.get_header(request)
            if header is None:
                raw_token = request.COOKIES.get(settings.AUTH_COOKIE)
            else:
                raw_token = self.get_raw_token(header)

            if raw_token is None:
                return None
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
        except Exception as e:  # pylint: disable=broad-except disable=unused-variable
            return None
