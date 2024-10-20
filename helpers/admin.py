"""Admin configuration"""

from django.contrib import admin
from helpers.models import ImageAsset

admin.site.register(ImageAsset)
