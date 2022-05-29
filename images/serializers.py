from email.mime import image

from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["url", "img_owner", "image", "date_added"]
