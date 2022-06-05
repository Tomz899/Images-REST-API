from django.conf import settings  # it's the correct way to import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from images.thumbs import basic_specs, premium_specs


class Image(models.Model):
    img_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=False)
    basic_thumb = ImageSpecField(**basic_specs)
    premium_thumb = ImageSpecField(**premium_specs)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]
