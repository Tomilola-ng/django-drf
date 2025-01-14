""" User Account Views """

from rest_framework import generics, response, status, permissions, views
from rest_framework_simplejwt.views import TokenObtainPairView

from django.conf import settings

from accounts.models import UserAccount
from accounts.serializers import LoginUserSerializer, CreateUserSerializer, UserSerializer


class LoginUserView(TokenObtainPairView):
    """
        Login User Endpoint
        - Requires Email and Password
        - returns JWT Tokens and User Data
    """
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        """ Post Request """
        data = super().post(request, *args, **kwargs)

        if data.status_code == 200:
            access_token = data.data.get('access')
            refresh_token = data.data.get('refresh')

            data.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            data.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response.Response({"message": "Login Successful",
                                  "data": data.data}, status=status.HTTP_200_OK)


class RegisterUserView(generics.CreateAPIView):
    """
        Create a new User Endpoint
    """
    queryset = UserAccount.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        """ Post Request """
        data = super().post(request, *args, **kwargs)
        return response.Response({"message": "User Created",
                                  "data": data.data}, status=status.HTTP_201_CREATED)


class CurrentUserView(views.APIView):
    """
        Get the current user
    """
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        """ Get Request """
        user = request.user
        data = self.serializer_class(user)
        return response.Response({"message": "User Retrieved",
                                  "data": data.data}, status=status.HTTP_200_OK)
