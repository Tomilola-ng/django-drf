"""Helper models"""

from django.db import models


class PageModel(models.Model):
    """Base model for all models"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    slug = models.ForeignKey(
        'SuperSlug', on_delete=models.CASCADE, related_name='page_slugs')

    objects = models.Manager()

    class Meta:
        """Meta options"""
        abstract = True
        ordering = ["-updated_at"]
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self) -> str:
        return f"{self.slug}"


class ImageAsset(models.Model):
    """Image Asset model"""
    image = models.ImageField(upload_to="image-assets/")
    alt = models.CharField(max_length=255, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        """Meta options"""
        verbose_name = "Image Asset"
        verbose_name_plural = "Image Assets"

    def __str__(self) -> str:
        return f"{self.image}"


class SuperSlug(models.Model):
    """Super Slug model"""
    slug = models.SlugField(unique=True)

    objects = models.Manager()

    class Meta:
        """Meta options"""
        abstract = True
        verbose_name = "Super Slug"
        verbose_name_plural = "Super Slugs"

    def __str__(self) -> str:
        return f"{self.slug}"
