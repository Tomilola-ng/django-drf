"""Helper views"""

from rest_framework import viewsets
from helpers.models import ImageAsset
from helpers.serilaizers import ImageAssetSerializer


class ImageAssetViewSet(viewsets.ModelViewSet):
    """Image Asset view set"""
    queryset = ImageAsset.objects.all()
    serializer_class = ImageAssetSerializer
