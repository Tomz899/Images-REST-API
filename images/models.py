from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    img_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    image = models.ImageField(null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_added"]
