from email.mime import image

from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="img_owner.username")

    class Meta:
        model = Image
        fields = ["url", "author", "img_owner", "image", "date_added"]
