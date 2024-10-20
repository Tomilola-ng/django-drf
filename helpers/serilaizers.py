"""Helper serializers"""

from rest_framework import serializers
from helpers.models import ImageAsset

class ImageAssetSerializer(serializers.ModelSerializer):
    """Image Asset serializer"""
    class Meta:
        """Meta options"""
        model = ImageAsset
        fields = "__all__"
