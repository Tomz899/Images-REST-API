from rest_framework import serializers
from easy_thumbnails_rest.serializers import ThumbnailerSerializer

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="img_owner.username")
    thumbnail = ThumbnailerSerializer(alias="basic")

    class Meta:
        model = Image
        fields = ["url", "author", "img_owner", "image", "thumbnail", "date_added"]
