""" User Account Serializers """

from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Define a serializer for UserAccount."""
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        """Define Meta options for UserSerializer."""
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
        ]

    def get_first_name(self, obj):
        """Return the first name of the user."""
        return obj.first_name.title()

    def get_last_name(self, obj):
        """Return the last name of the user."""
        return obj.last_name.title()

    def to_representation(self, instance):
        """Return the representation of the user."""
        representation = super(
            UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CreateUserSerializer(UserCreateSerializer):
    """Define a serializer for creating UserAccount."""
    class Meta(UserCreateSerializer.Meta):
        """Define Meta options for CreateUserSerializer."""
        model = User
        fields = ["id", "email", "first_name", "last_name", "password"]


class LoginUserSerializer(TokenObtainPairSerializer):  # pylint: disable=abstract-method
    """Define a serializer for login UserAccount."""

    def validate(self, attrs):
        """Validate the user credentials."""
        data = super().validate(attrs)
        user = self.user
        data.update({
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
            }
        })

        return data
