from django.conf import settings  # it's the correct way to import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from images.thumbs import basic_image_field_specs


class Image(models.Model):
    img_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=False)
    thumbnail = ImageSpecField(**basic_image_field_specs)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]
