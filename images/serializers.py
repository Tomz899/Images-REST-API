from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="img_owner.username")
    thumb = serializers.SerializerMethodField("get_thumb_url")

    class Meta:
        model = Image
        fields = ["url", "author", "img_owner", "image", "thumb", "date_added"]

    def get_thumb_url(self, obj):
        # Create thumbnail url and add absolute path for working link
        request = self.context.get("request")
        thumb_url = obj.thumbnail.url
        return request.build_absolute_uri(thumb_url)
