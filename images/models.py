from pathlib import Path

from django.conf import settings  # it's the correct way to import settings
from django.contrib.auth.models import User
from django.db import models
from PIL import Image as Img


class Image(models.Model):
    img_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    image = models.ImageField(null=True, blank=False)
    thumbnail = models.ImageField(upload_to="tumbs/", editable=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.image:
            self.thumbnail = None
        else:
            size = 128, 128

            im = Img.open(self.image)
            im.thumbnail(size)
            name = Path(self.image.name)
            # omit Path() if MEDIA_ROOT is already a Path object
            thb_path = Path(settings.MEDIA_ROOT) / f"thumb_{name.stem}.png"
            self.thumbnail = thb_path.name  # it's should be relative path

            im.save(thb_path, "PNG")  # if it doesn't like Path, str() it

        super(Image, self).save(force_insert, force_update, using, update_fields)
