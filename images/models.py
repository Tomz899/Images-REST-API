from pathlib import Path

from django.conf import settings  # it's the correct way to import settings

# from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# from easy_thumbnails.fields import ThumbnailerImageField
from PIL import Image as Img


class Image(models.Model):
    img_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=False)
    thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 80},
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     if not self.image:
    #         self.thumbnail = None
    #     else:
    #         size = 128, 128

    #         im = Img.open(self.image)
    #         im.thumbnail(size)
    #         name = Path(self.image.name)
    #         # omit Path() if MEDIA_ROOT is already a Path object
    #         thb_path = Path(settings.MEDIA_ROOT) / f"thumb_{name.stem}.png"
    #         self.thumbnail = thb_path.name  # it's should be relative path

    #         im.save(thb_path, "PNG")  # if it doesn't like Path, str() it

    #     super(Image, self).save(force_insert, force_update, using, update_fields)
